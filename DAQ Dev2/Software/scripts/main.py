#Time related operations
import time
from datetime import timedelta
from datetime import datetime

#GUI
from gcode_runner import GCodeRunner
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, pyqtSignal

#Serial devices
import list_uart_ports as list_uart_ports
from serial_device import SerialDevice
from grbl_device import GRBLDevice
from laser_sampler import LaserSampler

from gui.daq_dev2_gui import Ui_MainWindow

#Running GCODE
import gcode_parser 

import csv
import os

#Constant variables 
LASER_BAUD_RATE = 256000
DATA_LIMIT = 4000 # Maximum number of data entries
ROBOT_BAUD_RATE = 115200

CALIBRATION_TIME = 15000 
MAX_SAMPLE = 5
MAX_POINT = 40

#PyQt5 Thread
class win(QMainWindow):
    data_recording_is_finished = pyqtSignal()

    def __init__(self)->None:
        super().__init__()
        self.qtWindow = Ui_MainWindow()
        self.qtWindow.setupUi(self)

        #Button signal-slot
        self.qtWindow.pushButton_UART_connect.clicked.connect(self.connect_ports)
        self.qtWindow.pushButton_import_GCODE.clicked.connect(self.import_gcode)
        self.qtWindow.pushButton_start.clicked.connect(self.run_gcode)

        #GUI variables and lists
        self.ls_1_port_idx = None
        self.ls_2_port_idx = None
        self.rt_port_idx = None
        self.LASER_1_PORT = None
        self.LASER_2_PORT = None
        self.ROBOT_PORT = None
        #Serial Threads
        self.LASER_1_ser = None
        self.LASER_2_ser = None
        self.ROBOT_ser = None

        self.isStarting = True
        self.isLaserON = True
        self.isMoveing = True
        self.start_time = 0.0
        self.data_entries = []
        self.point = 0 
        self.sample = 0
        self.gcode_line = None
        self.sample_time = None
        self.folder_name = None

        #Scanning serial ports and adding them to the combobox list
        self.ports = list_uart_ports.list_uart_ports()
        for port in self.ports:
            self.qtWindow.comboBox_UART_Laser1.addItem(port.description)
            self.qtWindow.comboBox_UART_Laser2.addItem(port.description)
            self.qtWindow.comboBox_UART_Robot.addItem(port.description)


    def connect_ports (self):
        #Getting the ports' info 
        self.ls_1_port_idx = self.qtWindow.comboBox_UART_Laser1.currentIndex()
        self.ls_2_port_idx = self.qtWindow.comboBox_UART_Laser2.currentIndex()
        self.rt_port_idx = self.qtWindow.comboBox_UART_Robot.currentIndex()

        #Selecting the device info (COMx or /dev/ttyUSBx)
        self.LASER_1_PORT = self.ports[self.ls_1_port_idx].device
        self.LASER_2_PORT = self.ports[self.ls_2_port_idx].device
        self.ROBOT_PORT = self.ports[self.rt_port_idx].device

        #Connecting the Serial Ports
        if self.LASER_1_PORT and self.LASER_2_PORT and self.ROBOT_PORT:

            self.LASER_1_ser = SerialDevice(port_name=self.LASER_1_PORT, baudrate=LASER_BAUD_RATE)
            #self.LASER_1_ser.set_data_handler(self.LASER_1_data_handler)

            self.ROBOT_ser = GRBLDevice(port_name=self.ROBOT_PORT, baudrate=ROBOT_BAUD_RATE)

            self.LASER_1_ser.start()
            #self.LASER_2_ser.start()
            self.ROBOT_ser.start()

            print(f"Connected to {self.LASER_1_PORT} at {LASER_BAUD_RATE} baud.")
            #print(f"Connected to {self.LASER_2_PORT} at {LASER_BAUD_RATE} baud.")
            print(f"Connected to {self.ROBOT_PORT} at {ROBOT_BAUD_RATE} baud.")
        
        #Calibrating lasers after connecting
        self.calibration()

        # #Displaying the angle of incident
        # self.angle_update_timer = QTimer(self)
        # self.angle_update_timer.timeout.connect(self.getAngle)
        # self.angle_update_timer.start(1000) #Starting to display angle after calibration

        self.update_time_label = QTimer(self)
        self.update_time_label.timeout.connect(self.update_time)

    def calibration (self):
        self.qtWindow.pushButton_UART_connect.setEnabled(False)
        
        self.ROBOT_ser.send('G28') # Set 0-0 position
        self.LASER_1_ser.send(b'E') # Enable LASER_1
        
        self.qtWindow.label_Status.setText("Waiting for calibration ...")

        self.LASER_1_ser.send(b'C')  
        
        QTimer.singleShot(CALIBRATION_TIME, self.calibration_finish)

    def calibration_finish (self):
        self.qtWindow.label_Status.setText("Calibration was completed!")
        self.qtWindow.pushButton_UART_connect.setEnabled(True)
        self.qtWindow.pushButton_import_GCODE.setEnabled(True)

        
        self.LASER_1_ser.send(b'D') # Disenable LASER_1
        self.LASER_1_ser.flush_queue()

    
    def import_gcode(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File to Import GCODE",
            "",  # Starting directory
            "GCODE Files (*.gcode)"  # File filters
        )
        if file_path:
            self.qtWindow.label_imported_gcode.setText(f"Selected: {file_path}")
            self.gcode_line = gcode_parser.gcode_parser(file_path)  
            self.qtWindow.pushButton_start.setEnabled(True)
            self.qtWindow.label_Status.setText("GCODE file was imported.")
        else:
            self.qtWindow.label_Status.setText("Please import a GCODE file!")

    def update_time(self):
        elapsed_time = time.time() - self.start_time
        self.qtWindow.label_Timepassed.setText(str(timedelta(seconds=int(elapsed_time))))

    def update_progress_bar(self, percent):
        self.qtWindow.progressBar.setValue(percent)

    def on_gcode_finished(self):
        self.qtWindow.label_Status.setText("GCODE execution completed.")
        self.qtWindow.pushButton_start.setText("Start")
        self.qtWindow.pushButton_import_GCODE.setEnabled(True)
        self.isStarting = True
        self.update_time_label.stop()
        self.LASER_1_ser.send(b'D\n')
        self.ROBOT_ser.send(b'G0 X0 Y0\n')
        self.ROBOT_ser.send(b'G0 X0 Y0\n')

    def run_gcode(self):
        if self.isStarting:

            self.sample_time = "dataset_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
            self.folder_name = f"data_{self.start_time}"

            self.update_time_label.start(1000)
            self.start_time = time.time()

            self.qtWindow.label_Status.setText("Starting to sample")
            self.qtWindow.pushButton_start.setText("Stop")
            self.qtWindow.pushButton_import_GCODE.setEnabled(False)

            self.isStarting = False

            self.gcode_thread = GCodeRunner(self.gcode_line, self.LASER_1_ser, self.ROBOT_ser, parent=self)
            self.gcode_thread.gcode_status.connect(self.qtWindow.label_Status.setText)
            self.gcode_thread.gcode_position.connect(self.qtWindow.label_position.setText)
            self.gcode_thread.gcode_command.connect(self.qtWindow.label_Command.setText)

            self.gcode_thread.data_recording_sig.connect(self.data_record)
            self.data_recording_is_finished.connect(self.gcode_thread.run_next_gcode)

            self.gcode_thread.progress.connect(self.update_progress_bar)
            self.gcode_thread.finished.connect(self.on_gcode_finished)
            self.gcode_thread.start()


        else:
            self.update_time_label.stop()
            self.start_time = 0.0
            self.qtWindow.label_Status.setText("Stopped sampling")
            self.qtWindow.pushButton_start.setText("Start")
            self.qtWindow.pushButton_import_GCODE.setEnabled(True)
            self.isStarting = True
            if hasattr(self, 'gcode_thread'): 
                self.gcode_thread.stop()

            if hasattr(self, 'sampler_thread') and self.sampler_thread.isRunning():
                self.sampler_thread.stop()
                self.sampler_thread.wait()

            self.ROBOT_ser.send(b'G0 X0 Y0')

    def data_record(self, movement, laser):
        #print("Starting threaded data recording...")
        self.isLaserON = laser
        self.isMoveing = movement

        if self.point < MAX_POINT:
            self.point = self.point + 1
        else:
            self.sample = self.sample + 1
            self.point = 0

        if self.sample == MAX_SAMPLE:
            print("MAX_SAMPLE Reached!")
            self.data_recording_is_finished.emit()  

        else:
            # Create and start laser sampling thread
            self.LASER_1_ser.flush_queue()
            self.sampler_thread = LaserSampler(self.LASER_1_ser, laser_on=laser, data_limit=DATA_LIMIT)
            self.sampler_thread.data_captured.connect(self.save_csv)  # Replace with saving logic
            self.sampler_thread.finished.connect(self.on_sampling_finished)

            self.sampler_thread.start()


    def on_sampling_finished(self):
        #print("Data sampling completed.")
        self.sampler_thread.stop()     
        self.data_recording_is_finished.emit()  

        os.makedirs(self.sample_time, exist_ok=True)

        # Save data to a CSV file
        file_name = f"data_{self.sample}_{self.point}.csv"
        full_path = os.path.join(self.sample_time, file_name)
        with open(full_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["DIST", "AMP", "TEMP", "VOLT","Timestamp", "Angle", "ON", "Movement"])
            writer.writerows(self.data_entries)
        #print(f"Saved {len(data_entries)} entries to {file_name}.")
        self.data_entries = []
        

    def save_csv(self, data_line):
        # Assume data_line format: 'id;[val1];id;[val2];...'
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            
            parts = data_line.split(';')
            numerical_values = []
            
            for i in range(1, len(parts), 2):  # Access only the '[value]' parts
                value = parts[i].strip().replace('[', '').replace(']', '')
                numerical_values.append(value)

            # Append to data_entries with timestamp, angle, laser and movement state
            row = numerical_values + [
                timestamp,
                self.getAngle(),
                self.isLaserON,
                self.isMoveing
            ]
            self.data_entries.append(row)

            print(len(self.data_entries))

        except Exception as e:
            print(f"Failed to save line: {data_line} — Error: {e}")

    def getAngle (self) -> float:
        return 90.0

    #     #self.LASER_1_ser.send(b'E')
    #     #self.LASER_2_ser.send(b'E')
        
    #     line_of_LASER_1 = self.LASER_1_data_queue.get()
    #     #line_of_LASER_2 = self.LASER_2_PORT.readline().decode('utf-8').strip()

    #     split_of_LASER_1 = line_of_LASER_1.split(';')
    #     #split_of_LASER_2 = line_of_LASER_2.split(';')

    #     length_R = float(split_of_LASER_1[1])
    #     length_L = float(random.randint(0,500) / 10) #split_of_LASER_2[1]

    #     distance_between = 19.5
    #     measurement_difference = length_R - length_L

    #     if measurement_difference != 0:
    #         angle = math.atan(distance_between / measurement_difference)
    #     else:
    #         angle = 0
            
    #     angle = angle * 180 / math.pi

    #     self.qtWindow.label_angle.setText(str(angle))

    #     return angle
    

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    window.show()
    app.exec()