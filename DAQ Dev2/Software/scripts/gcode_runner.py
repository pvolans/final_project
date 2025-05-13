from PyQt5.QtCore import QThread, pyqtSignal
import queue
from laser_sampler import LaserSampler

class GCodeRunner(QThread):
    gcode_status = pyqtSignal(str)
    gcode_position = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, gcode_lines, laser_ser, robot_ser, parent=None):
        super().__init__(parent)
        self.gcode_lines = gcode_lines
        self.laser_ser = laser_ser
        self.robot_ser = robot_ser
        self._running = True

    def stop(self):
        self._running = False

    def wait_for_grbl_ok(self, timeout=2.0):
        try:
            while True:
                response = self.robot_ser.queue.get(timeout=timeout)
                print(f"[GRBL] Response: {response}")
                if response.strip() == "ok":
                    return True
                elif response.startswith("error"):
                    print(f"[GRBL ERROR] {response}")
                    return False
                
        except queue.Empty:
            print("[GRBL TIMEOUT] No response from GRBL")
            return False     
           
    def run(self):
        for gcode_command in self.gcode_lines:
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

                if not self.wait_for_grbl_ok():
                    print("Aborting due to GRBL error")
                    break
            
            self.gcode_position.emit(self.laser_ser.queue.get())


        self.finished.emit()
