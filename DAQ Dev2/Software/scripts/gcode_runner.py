from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QTimer
import queue
import time

class GCodeRunner(QThread):
    gcode_status = pyqtSignal(str)
    gcode_position = pyqtSignal(str)
    finished = pyqtSignal()
    progress = pyqtSignal(int)  


    def __init__(self, gcode_lines, laser_ser, robot_ser, parent=None):
        super().__init__(parent)
        self.gcode_lines = gcode_lines
        self.laser_ser = laser_ser
        self.robot_ser = robot_ser
        self._running = True
        self._ok = False

    def stop(self):
        self.finished.emit()
        self._running = False


    def run(self):
        total_lines = len(self.gcode_lines)

        for i, gcode_command in enumerate(self.gcode_lines):
            if not self._running:
                break
            

            first_word = gcode_command.split()[0]

            if first_word == "M4":
                self.laser_ser.send(b'E')
                self.gcode_status.emit("Sampling with Laser")
              

            elif first_word == "M5":
                self.laser_ser.send(b'L')
                self.gcode_status.emit("Sampling without Laser")
                

            elif first_word == "G0":
                self.robot_ser.send(gcode_command + '\n')
                self.gcode_status.emit(gcode_command)

                if self.wait_for_grbl_ok():

                    if not self.wait_until_idle():
                        print("Aborting due to GRBL IDLE error")
                        break
                else: 
                    print("Aborting due to GRBL ok response error")
                    break
            # Emit progress
            progress_percent = int((i + 1) / total_lines * 100)
            self.progress.emit(progress_percent)
            
            
        self.stop()

    def wait_until_idle(self, timeout=10):
        start = time.time()
        while time.time() - start < timeout:
            self.robot_ser.send(b"?")
            time.sleep(0.1)
            response = self.robot_ser.queue.get()
            if response.startswith("<") and "Idle" in response:
                return True
        return False
    
    
    def wait_for_grbl_ok(self, timeout=2.0):
        """Non-blocking GRBL OK checker with timeout in seconds"""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if not self._running:
                return False  # stop immediately if thread is asked to stop

            try:
                response = self.robot_ser.queue.get_nowait()
                print(f"[GRBL] Response: {response}")

                if response.strip() == "ok":
                    return True
                elif response.startswith("error"):
                    print(f"[GRBL ERROR] {response}")
                    return False
            except queue.Empty:
                time.sleep(0.01)  # yield control briefly to avoid busy-waiting


