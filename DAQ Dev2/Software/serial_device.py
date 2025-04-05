import serial
from PyQt5.QtCore import QThread, pyqtSignal

class serial_device(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port_name, baudrate=115200):
        super().__init__()
        self.port_name = port_name
        self.baudrate = baudrate
        self._running = True
        self.ser = None

    def run(self):
        self.ser = serial.Serial(self.port_name, self.baudrate, timeout=0.1)
        while self._running:
            if self.ser.in_waiting:
                data = self.ser.readline().decode().strip()
                if data:
                    self.data_received.emit(data)

    def send(self, msg):
        if self.ser and self.ser.is_open:
            self.ser.write(msg.encode())

    def stop(self):
        self._running = False
        if self.ser:
            self.ser.close()
        self.quit()
        self.wait()