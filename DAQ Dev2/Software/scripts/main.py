import math

#Time related operations
import time
import csv
from datetime import timedelta

#GUI
from gcode_runner import GCodeRunner
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

#Serial devices
import list_uart_ports as list_uart_ports
from serial_device import SerialDevice
from grbl_device import GRBLDevice
import queue

from gui.daq_dev2_gui import Ui_MainWindow

#Running GCODE
import gcode_parser 

#Testing
import random

#Constant variables 
LASER_BAUD_RATE = 256000
DATA_LIMIT = 4000  # Maximum number of data entries
ROBOT_BAUD_RATE = 115200

CALIBRATION_TIME = 1000 # 13000

#PyQt5 Thread
class win(QMainWindow):
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
        self.start_time = 0.0
        self.data_entries = []
        self.point = 0 
        self.sample = 0
        self.gcode_line = None

        #Serial data queue to handle shared resources
        self.LASER_1_data_queue = queue.Queue()
        self.ROBOT_data_queue = queue.Queue()

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
            self.LASER_1_ser.set_data_handler(self.LASER_1_data_handler)

            self.ROBOT_ser = GRBLDevice(port_name=self.ROBOT_PORT, baudrate=ROBOT_BAUD_RATE)

            self.LASER_1_ser.start()
            #self.LASER_2_ser.start()
            self.ROBOT_ser.start()

            print(f"Connected to {self.LASER_1_PORT} at {LASER_BAUD_RATE} baud.")
            #print(f"Connected to {self.LASER_2_PORT} at {LASER_BAUD_RATE} baud.")
            print(f"Connected to {self.ROBOT_PORT} at {ROBOT_BAUD_RATE} baud.")
        
        #Calibrating lasers after connecting
        self.calibration()

        #Displaying the angle of incident
        self.angle_update_timer = QTimer(self)
        self.angle_update_timer.timeout.connect(self.getAngle)
        self.angle_update_timer.start(1000) #Starting to display angle after calibration

        self.label_update_timer = QTimer(self)
        self.label_update_timer.timeout.connect(self.update_labels)
        self.label_update_timer.start(100)

        self.update_time_label = QTimer(self)
        self.update_time_label.timeout.connect(self.update_time)

    def calibration (self):
        self.qtWindow.pushButton_UART_connect.setEnabled(False)
        
        self.ROBOT_ser.send('G28') # Set 0-0 position
        self.LASER_1_ser.send(b'E') # Enable LASER_1
        #self.LASER_2_ser.send(b'E') # Enable LASER_2
        
        self.qtWindow.label_Status.setText("Waiting for calibration ...")

        self.LASER_1_ser.send(b'C')  
        # self.LASER_2_ser.send(b'C')
        QTimer.singleShot(CALIBRATION_TIME, self.calibration_finish)

    def calibration_finish (self):
        self.qtWindow.label_Status.setText("Calibration was completed!")
        self.qtWindow.pushButton_UART_connect.setEnabled(True)
        self.qtWindow.pushButton_import_GCODE.setEnabled(True)

    
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

    def update_labels(self):
        pass
#-----------------------------------------------------------------------------------------------------
    def run_gcode(self):
        if self.isStarting:
            self.update_time_label.start(1000)
            self.start_time = time.time()
            self.qtWindow.label_Status.setText("Starting to sample")
            self.qtWindow.pushButton_start.setText("Stop")
            self.qtWindow.pushButton_import_GCODE.setEnabled(False)
            self.isStarting = False

            self.gcode_thread = GCodeRunner(self.gcode_line, self.LASER_1_ser, self.ROBOT_ser)
            self.gcode_thread.gcode_status.connect(self.qtWindow.label_Status.setText)
            self.gcode_thread.gcode_position.connect(self.qtWindow.label_position.setText)
            self.gcode_thread.gcode_command.connect(self.qtWindow.label_Command.setText)
            self.gcode_thread.progress.connect(self.update_progress_bar)
            self.gcode_thread.finished.connect(self.on_gcode_finished)
            self.gcode_thread.start()


        else:
            self.update_time_label.stop()
            self.start_time = 0.0
            self.qtWindow.label_Status.setText("Stopped sampling")
            self.qtWindow.pushButton_start.setText("Start")
            self.qtWindow.pushButton_import_GCODE.setEnabled(True)
            self.ROBOT_ser.send(b'G0 X0 Y0')
            self.isStarting = True
            if hasattr(self, 'gcode_thread'):
                self.gcode_thread.stop()
                

    def LASER_1_data_handler(self):
        while not self.LASER_1_ser.queue.empty():
            data = self.LASER_1_ser.queue.get()
            if data:
                self.LASER_1_data_queue.put(data)

                
    def getAngle (self) -> float:

        #self.LASER_1_ser.send(b'E')
        #self.LASER_2_ser.send(b'E')
        
        line_of_LASER_1 = self.LASER_1_data_queue.get()
        #line_of_LASER_2 = self.LASER_2_PORT.readline().decode('utf-8').strip()

        split_of_LASER_1 = line_of_LASER_1.split(';')
        #split_of_LASER_2 = line_of_LASER_2.split(';')

        length_R = float(split_of_LASER_1[1])
        length_L = float(random.randint(0,500) / 10) #split_of_LASER_2[1]

        distance_between = 19.5
        measurement_difference = length_R - length_L

        if measurement_difference != 0:
            angle = math.atan(distance_between / measurement_difference)
        else:
            angle = 0
            
        angle = angle * 180 / math.pi

        self.qtWindow.label_angle.setText(str(angle))

        return angle
    
    def LASER_2_data_handler(self):
        pass
    

    def ROBOT_data_handler(self):
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = win()
    window.show()
    app.exec()