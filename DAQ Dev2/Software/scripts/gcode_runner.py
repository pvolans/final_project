#gcode_runner.py
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition, QCoreApplication, pyqtSignal, pyqtSlot
import time

class GCodeRunner(QThread):
    gcode_status = pyqtSignal(str)
    gcode_position = pyqtSignal(str)
    gcode_command = pyqtSignal(str)
    data_recording_sig = pyqtSignal(bool, bool)
    finished = pyqtSignal()
    progress = pyqtSignal(int)  


    def __init__(self, gcode_lines, laser_ser, robot_ser, parent=None):
        super().__init__(parent)
        self.gcode_lines = gcode_lines
        self.laser_ser = laser_ser
        self.robot_ser = robot_ser
        self._running = True
        self._ok = False
        self._idle = True
        self._run = False
        self.mutex_robot_status = QMutex()

        #Robot status reading
        self.robot_ser.ok_received.connect(self.handle_ok)
        self.robot_ser.idle_detected.connect(self.handle_idle)
        self.robot_ser.run_detected.connect(self.handle_run)
        self.robot_ser.error_received.connect(self.handle_error)

        #Sampling process
        self._laser_on = False
        self._movement = False
        self._data_is_recorded = False
        self.mutex_is_recording = QMutex()
        self._data_recording_wait = QWaitCondition()


    def handle_ok(self):
        with QMutexLocker(self.mutex_robot_status):
            self._ok = True

    def handle_idle(self, data):
        with QMutexLocker(self.mutex_robot_status):
            self._idle = True
        
        self.gcode_position.emit(data)

    def handle_run(self):
        with QMutexLocker(self.mutex_robot_status):
            self._run = True

    def handle_error(self, msg):
        self.stop()

    def stop(self):
        self._running = False
        self.finished.emit()


    def run(self):
        total_lines = len(self.gcode_lines)

        for i, gcode_command in enumerate(self.gcode_lines):
            if not self._running:
                break
            
            self.gcode_command.emit(gcode_command)

            first_word = gcode_command.split()[0]

            if first_word == "G0":
                with QMutexLocker(self.mutex_robot_status):
                    self._ok = False
                    self._idle = False
                    self._run = False

                self.robot_ser.send(gcode_command + '\n')

                if not self.wait_for_flag(lambda: self._ok, timeout=3):
                    print("Timeout waiting for GRBL ok")

            elif first_word == "M4":
                self._laser_on = True
                self.gcode_status.emit("Sampling with Laser")

            elif first_word == "M5":
                self._laser_on = False
                self.gcode_status.emit("Sampling without Laser")

            elif first_word == "G4":
                self.robot_ser.send(gcode_command + '\n')
                if not self.wait_for_flag(lambda: self._ok, timeout=3):
                    print("Timeout waiting for GRBL ok")

            elif first_word == "M100":
                self.gcode_status.emit("Sampling with Movement")
                self._movement = True

                # Initialize next_1 and next_2 to None
                next_gcode_1 = None
                next_gcode_2 = None

                # Search for next_1 that starts with "G0"
                for j in range(i + 1, len(self.gcode_lines)):
                    if self.gcode_lines[j].startswith("G0"):
                        next_gcode_1 = self.gcode_lines[j]
                        break
                # Search for next_2 after next_1
                if next_gcode_1:
                    for k in range(j + 1, len(self.gcode_lines)):
                        if self.gcode_lines[k].startswith("G0"):
                            next_gcode_2 = self.gcode_lines[k]
                            i = k #Do not run the repeated gcode after the loop 
                            break
                
                if next_gcode_1 is None and next_gcode_2 is None:
                    self.gcode_status.emit("Missing next G0 in M100 sequence")
                    break

                with QMutexLocker(self.mutex_robot_status):
                    self._ok = False
                self.robot_ser.send(next_gcode_1 + '\n')
                if not self.wait_for_flag(lambda: self._ok, timeout=3):
                    print("Timeout waiting for GRBL ok")
                    
                with QMutexLocker(self.mutex_robot_status):
                    self._ok = False
                self.robot_ser.send('G4 P0\n')
                if not self.wait_for_flag(lambda: self._ok, timeout=3):
                    print("Timeout waiting for GRBL ok")
                        
                self.data_recording_sig.emit(self._movement, self._laser_on)

                data_is_recorded = False
                while not data_is_recorded:


                    with QMutexLocker(self.mutex_robot_status):
                        self._ok = False
                    self.robot_ser.send(next_gcode_2 + '\n')
                    if not self.wait_for_flag(lambda: self._ok, timeout=3):
                        print("Timeout waiting for GRBL ok")

                    with QMutexLocker(self.mutex_robot_status):
                        self._ok = False
                    self.robot_ser.send('G4 P0\n')
                    if not self.wait_for_flag(lambda: self._ok, timeout=3):
                        print("Timeout waiting for GRBL ok")

                    with QMutexLocker(self.mutex_robot_status):
                        self._ok = False
                    self.robot_ser.send(next_gcode_1 + '\n')
                    if not self.wait_for_flag(lambda: self._ok, timeout=3):
                        print("Timeout waiting for GRBL ok")

                    with QMutexLocker(self.mutex_robot_status):
                        self._ok = False
                    self.robot_ser.send('G4 P0\n')
                    if not self.wait_for_flag(lambda: self._ok, timeout=3):
                        print("Timeout waiting for GRBL ok")
                        
                    with QMutexLocker(self.mutex_is_recording):
                        data_is_recorded = self._data_is_recorded

                    QCoreApplication.processEvents()

                self._data_is_recorded = False

            elif first_word == "M101":
                self.gcode_status.emit("Sampling without Movement")
                self._movement = True
                self.data_recording_sig.emit(self._movement, self._laser_on)
                with QMutexLocker(self.mutex_is_recording):
                    while not self._data_is_recorded:
                        self._data_recording_wait.wait(self.mutex_is_recording)
                        
                    self._data_is_recorded = False

            else:
                self.robot_ser.send(gcode_command + '\n')
            

            # Emit progress
            progress_percent = int((i + 1) / total_lines * 100)
            self.progress.emit(progress_percent)
            
            
        self.stop()

    @pyqtSlot()
    def run_next_gcode(self):
        with QMutexLocker(self.mutex_is_recording):
            self._data_is_recorded = True
            self._data_recording_wait.wakeAll()

    def wait_for_flag(self, check_fn, timeout=5):
        """Wait until check_fn() returns True or timeout occurs."""
        start = time.time()
        while time.time() - start < timeout:
            with QMutexLocker(self.mutex_robot_status):
                if check_fn():
                    return True
            time.sleep(0.01)
        return False
