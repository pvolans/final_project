from PyQt5.QtCore import QThread, pyqtSignal
import time

class LaserSampler(QThread):
    sample_ready = pyqtSignal(object)

    def __init__(self, laser_queue, data_entries, get_angle_func):
        super().__init__()
        self.laser_queue = laser_queue
        self.data_entries = data_entries
        self.get_angle_func = get_angle_func
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            if not self.laser_queue.empty():
                line = self.laser_queue.get().decode('utf-8').strip()
                if line:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                    angle = self.get_angle_func()
                    parts = line.split(';')
                    values = [parts[i].replace('[', '').replace(']', '') for i in range(1, len(parts), 2)]
                    self.data_entries.append(values + [timestamp, angle])
                    self.sample_ready.emit(values)

    def stop(self):
        self.running = False
        self.quit()
        self.wait()