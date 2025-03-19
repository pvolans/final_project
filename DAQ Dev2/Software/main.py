import list_uart_ports
#import time
#import csv
#from datetime import datetime
#import os
#import gcode_parser 

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from daq_dev2_gui import Ui_MainWindow

class win(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.qtWindow = Ui_MainWindow()
        self.qtWindow.setupUi(self)
        #self.qtWindow.pushButton_UART_connect.clicked.connect(self.list_uart_ports)

if __name__ == "__main__":
    app = QApplication([])
    window = win()

    ports = list_uart_ports.list_uart_ports()
    for port in ports:
        window.qtWindow.comboBox_UART_Laser1.addItem(port.description)
        window.qtWindow.comboBox_UART_Laser2.addItem(port.description)
        window.qtWindow.comboBox_UART_Robot.addItem(port.description)

    window.show()
    app.exec()



