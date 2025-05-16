# serial_device.py
import serial
from PyQt5.QtCore import QThread, QMutex, pyqtSignal
import queue

class serial_device(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, data_handler, port_name, baudrate=115200):
        super().__init__()
        self.port_name = port_name
        self.baudrate = baudrate
        self._running = True
        self.ser = None
        self.queue = queue.Queue()

        self.data_received.connect(data_handler)
        self.mutex_ser = QMutex()

    def run(self):
        try:
            self.ser = serial.Serial(self.port_name, self.baudrate, timeout=0.1)


        except serial.SerialException as e:
            print(f"[ERROR] Could not open {self.port_name}: {e}")
            return

        while self._running:
            try:
                if self.ser.in_waiting:
                    data = self.ser.readline()

                    if data:
                        decoded = data.decode(errors='ignore').strip()
                        self.queue.put(decoded)
                        self.data_received.emit(decoded)

            except serial.SerialException as e:
                print(f"[ERROR] SerialException: {e}")
                break

    def send(self, msg):
            if self.ser and self.ser.is_open:
                if isinstance(msg, str):
                    msg = msg.encode()
                    
                self.mutex_ser.lock()
                try:
                    self.ser.write(msg)
                finally:
                    self.mutex_ser.unlock()

    def stop(self):
        self._running = False
        if self.ser and self.ser.is_open:
            self.mutex_ser.lock()
            try:
                self.ser.close()
            finally:
                self.mutex_ser.unlock()

        self.quit()
        self.wait()
