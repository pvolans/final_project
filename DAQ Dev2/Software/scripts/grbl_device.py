#grbl_device.py
from PyQt5.QtCore import QTimer, pyqtSignal
import queue
import time
from serial_device import SerialDevice

class GRBLDevice(SerialDevice):
    ok_received = pyqtSignal()
    idle_detected = pyqtSignal(str)
    run_detected = pyqtSignal()
    error_received = pyqtSignal(str)

    def __init__(self, port_name, baudrate, parent=None):
        super().__init__(port_name=port_name, baudrate=baudrate)
        self.set_data_handler(self.grbl_data_handler)

        # self.status_timer = QTimer(self)
        # self.status_timer.setInterval(1)
        # self.status_timer.timeout.connect(lambda: self.send(b"?"))
        # self.status_timer.start()

    def grbl_data_handler(self, line: str):
        line = self.queue.get()
        #print(f"[GRBL] Response: {line}")


        if line.strip() == "ok":
            self.ok_received.emit()
            print("ok responded")

        elif line.startswith("error"):
            #print(f"[GRBL ERROR] {line}")
            self.error_received.emit(line)

        elif line.startswith("<") and "Idle" in line:
            self.idle_detected.emit(line)
            #print("idle responded")

        elif line.startswith("<") and "Run" in line:
            self.run_detected.emit()

    def stop(self):
        super().stop()
        self.status_timer.stop()