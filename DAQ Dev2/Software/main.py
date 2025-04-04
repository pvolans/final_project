import list_uart_ports
import serial
import time

#import csv
#from datetime import datetime
#import os
#import gcode_parser 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from daq_dev2_gui import Ui_MainWindow

LASER_BAUD_RATE = 256000
DATA_LIMIT = 4000  # Maximum number of data entries
ROBOT_BAUD_RATE = 115200

class win(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.qtWindow = Ui_MainWindow()
        self.qtWindow.setupUi(self)
        self.qtWindow.pushButton_UART_connect.clicked.connect(self.connect_ports)
        self.ls_1_port_idx = None
        self.ls_2_port_idx = None
        self.rt_port_idx = None
        self.LASER_1_PORT = None
        self.LASER_2_PORT = None
        self.ROBOT_PORT = None
        self.LASER_1_ser = None
        self.LASER_2_ser = None
        self.ROBOT_ser = None

        self.ports = list_uart_ports.list_uart_ports()
        for port in self.ports:
            self.qtWindow.comboBox_UART_Laser1.addItem(port.description)
            self.qtWindow.comboBox_UART_Laser2.addItem(port.description)
            self.qtWindow.comboBox_UART_Robot.addItem(port.description)


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
        """
        self.ROBOT_PORT.write(b'G28') # Set 0-0 position
        self.LASER_1_PORT.write(b'E') # Enable LASER_1
        self.LASER_2_PORT.write(b'E') # Enable LASER_1
        """
        self.qtWindow.label_Status.setText("Waiting for calibration ...")
        QTimer.singleShot(13000, lambda: self.qtWindow.label_Status.setText("Calibration was completed ..."))

        """self.LASER_1_PORT.write(b'C')  
        self.LASER_2_PORT.write(b'C')    """           
             




if __name__ == "__main__":
    app = QApplication([])
    window = win()
    window.show()
    app.exec()



