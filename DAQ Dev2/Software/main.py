import list_uart_ports
import math
import random
#import csv
#from datetime import datetime
#import os
import gcode_parser 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from daq_dev2_gui import Ui_MainWindow

LASER_BAUD_RATE = 256000
DATA_LIMIT = 4000  # Maximum number of data entries
ROBOT_BAUD_RATE = 115200

CALIBRATION_TIME = 1000 # 13000

class win(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.qtWindow = Ui_MainWindow()
        self.qtWindow.setupUi(self)

        self.qtWindow.pushButton_UART_connect.clicked.connect(self.connect_ports)
        self.qtWindow.pushButton_import_GCODE.clicked.connect(self.import_gcode)
        self.qtWindow.pushButton_start.clicked.connect(self.run_gcode)

        self.ls_1_port_idx = None
        self.ls_2_port_idx = None
        self.rt_port_idx = None
        self.LASER_1_PORT = None
        self.LASER_2_PORT = None
        self.ROBOT_PORT = None
        self.LASER_1_ser = None
        self.LASER_2_ser = None
        self.ROBOT_ser = None
        self.isStarting = True

        self.ports = list_uart_ports.list_uart_ports()
        for port in self.ports:
            self.qtWindow.comboBox_UART_Laser1.addItem(port.description)
            self.qtWindow.comboBox_UART_Laser2.addItem(port.description)
            self.qtWindow.comboBox_UART_Robot.addItem(port.description)

        self.angle_update_timer = QTimer(self)
        self.angle_update_timer.timeout.connect (self.getAngle)
        self.angle_update_timer.start(1000)

        self.gcode_line = None



    def connect_ports (self):
        self.ls_1_port_idx = self.qtWindow.comboBox_UART_Laser1.currentIndex()
        self.ls_2_port_idx = self.qtWindow.comboBox_UART_Laser2.currentIndex()
        self.rt_port_idx = self.qtWindow.comboBox_UART_Robot.currentIndex()

        #self.LASER_1_PORT = self.ports[self.ls_1_port_idx].device
        #self.LASER_2_PORT = self.ports[self.ls_2_port_idx].device
        #self.ROBOT_PORT = self.ports[self.rt_port_idx].device
        if True: #with serial.Serial(window.LASER_1_PORT, LASER_BAUD_RATE, timeout=1) as self.LASER_1_ser, \
        #serial.Serial(window.LASER_2_PORT, LASER_BAUD_RATE, timeout=1) as self.LASER_2_ser, \
        #serial.Serial(window.ROBOT_PORT, ROBOT_BAUD_RATE, timeout=1) as self.ROBOT_ser:
            print(f"Connected to {window.LASER_1_PORT} at {LASER_BAUD_RATE} baud.")
            print(f"Connected to {window.LASER_2_PORT} at {LASER_BAUD_RATE} baud.")
            print(f"Connected to {window.ROBOT_PORT} at {ROBOT_BAUD_RATE} baud.")
        
        self.calibration()




    def calibration (self):
        self.qtWindow.pushButton_UART_connect.setEnabled(False)
        """
        self.ROBOT_PORT.write(b'G28') # Set 0-0 position
        self.LASER_1_PORT.write(b'E') # Enable LASER_1
        self.LASER_2_PORT.write(b'E') # Enable LASER_2
        """
        self.qtWindow.label_Status.setText("Waiting for calibration ...")

        """self.LASER_1_PORT.write(b'C')  
        self.LASER_2_PORT.write(b'C')    """   
        QTimer.singleShot(CALIBRATION_TIME, self.calibration_finish)

    def calibration_finish (self):
        self.qtWindow.label_Status.setText("Calibration was completed!")
        self.qtWindow.pushButton_UART_connect.setEnabled(True)
        self.qtWindow.pushButton_import_GCODE.setEnabled(True)

        


    def getAngle (self) -> float:

        #self.LASER_1_PORT.write(b'E')
        #self.LASER_2_PORT.write(b'E')
        
        #line_of_LASER_1 = self.LASER_1_PORT.readline().decode('utf-8').strip()
        #line_of_LASER_2 = self.LASER_2_PORT.readline().decode('utf-8').strip()

        #split_of_LASER_1 = line_of_LASER_1.split(';')
        #split_of_LASER_2 = line_of_LASER_2.split(';')

        length_R = 0.0#split_of_LASER_1[1]
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



    def run_gcode(self):

        if self.isStarting:
            self.qtWindow.label_Status.setText("Starting to sample")
            self.qtWindow.pushButton_start.setText("Stop")
            self.qtWindow.pushButton_import_GCODE.setEnabled(False)
            self.isStarting = False

            for gcode_command in self.gcode_line:
                self.qtWindow.label_Command.setText(gcode_command)
                print(gcode_command)
        else:
            self.qtWindow.label_Status.setText("Stoped to sample")
            self.qtWindow.pushButton_start.setText("Start")
            self.qtWindow.pushButton_import_GCODE.setEnabled(True)
            self.isStarting = True





             


if __name__ == "__main__":
    app = QApplication([])
    window = win()
    window.show()
    app.exec()



