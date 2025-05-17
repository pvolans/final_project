#gcode_runner.py
from PyQt5.QtCore import QThread, QMutex, QMutexLocker, pyqtSignal
import time

class GCodeRunner(QThread):
    gcode_status = pyqtSignal(str)
    gcode_position = pyqtSignal(str)
    gcode_command = pyqtSignal(str)
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
        self.mutex = QMutex()

        self.robot_ser.ok_received.connect(self.handle_ok)
        self.robot_ser.idle_detected.connect(self.handle_idle)
        self.robot_ser.run_detected.connect(self.handle_run)
        self.robot_ser.error_received.connect(self.handle_error)


    def handle_ok(self):
        with QMutexLocker(self.mutex):
            self._ok = True

    def handle_idle(self, data):
        with QMutexLocker(self.mutex):
            self._idle = True
        
        self.gcode_position.emit(data)

    def handle_run(self):
        with QMutexLocker(self.mutex):
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
                with QMutexLocker(self.mutex):
                    self._ok = False
                    self._idle = False
                    self._run = False

                self.robot_ser.send(gcode_command + '\n')

                if not self.wait_for_flag(lambda: self._ok, timeout=3000):
                    print("Timeout waiting for GRBL ok")
                    # Wait for idle

                if not self.wait_for_flag(lambda: self._idle, timeout=1000):
                    print("Timeout waiting for GRBL idle")
                    break


            elif first_word == "M4":
                self.laser_ser.send(b'E')
                self.gcode_status.emit("Sampling with Laser")
              

            elif first_word == "M5":
                self.laser_ser.send(b'L')
                self.gcode_status.emit("Sampling without Laser")

            # Emit progress
            progress_percent = int((i + 1) / total_lines * 100)
            self.progress.emit(progress_percent)
            
            
        self.stop()

    def wait_for_flag(self, check_fn, timeout=5):
        """Wait until check_fn() returns True or timeout occurs."""
        start = time.time()
        while time.time() - start < timeout:
            with QMutexLocker(self.mutex):
                if check_fn():
                    return True
            time.sleep(0.005)
        return False
