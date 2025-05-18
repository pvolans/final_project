from PyQt5.QtCore import QThread, pyqtSignal, QMutex, QMutexLocker, QWaitCondition, QCoreApplication
import csv
from datetime import datetime

class LaserSampler(QThread):
    data_captured = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, laser_device, laser_on=True, data_limit=4000, parent=None):
        super().__init__(parent)
        self.laser = laser_device
        self.laser_on = laser_on
        self.data_limit = data_limit
        self.running = True

        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()

    def run(self):
        sample_count = 0

        while self.running and sample_count < self.data_limit:
            # Send sampling command
            self.laser.send(b'E' if self.laser_on else b'L')

            # Wait for data using a wait condition instead of time.sleep
            with QMutexLocker(self.mutex):
                if self.laser.queue.empty():
                    self.wait_condition.wait(self.mutex, 2000)  # wait max 2000 ms

            if not self.running:
                break

            if not self.laser.queue.empty():
                data = self.laser.queue.get()
                if data:

                    self.data_captured.emit(data)
                    sample_count += 1
                    #print(f"sampled: {sample_count}")
            else:
                print("Timeout waiting for laser data.")
                break
            
            QCoreApplication.processEvents()

        # Turn off laser and clean up
        self.laser.send(b'D')
        self.laser.flush_queue()
        self.finished.emit()

    def stop(self):
        self.running = False
        self.wait_condition.wakeAll()
        self.quit()
        self.wait()
