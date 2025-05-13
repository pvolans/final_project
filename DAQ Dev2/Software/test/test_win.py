import unittest
import sys
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

# Import the original class (assuming the file is named main.py)
from main import win, LASER_BAUD_RATE, ROBOT_BAUD_RATE, DATA_LIMIT

class TestWinClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication for testing GUI components"""
        cls.app = QApplication(sys.argv)

    def setUp(self):
        """Create a fresh instance of the win class before each test"""
        self.window = win()

    def tearDown(self):
        """Clean up after each test"""
        self.window.close()

    def test_initial_state(self):
        """Test the initial state of the window"""
        # Check initial variables
        self.assertIsNone(self.window.ls_1_port_idx)
        self.assertIsNone(self.window.ls_2_port_idx)
        self.assertIsNone(self.window.rt_port_idx)
        self.assertTrue(self.window.isStarting)
        self.assertTrue(self.window.isLaserON)
        self.assertEqual(len(self.window.data_entries), 0)
        self.assertEqual(self.window.point, 0)
        self.assertEqual(self.window.sample, 0)

    def test_connect_ports(self):
        """Test the connect_ports method"""
        # Mock the serial devices to avoid actual serial communication
        with patch('main.serial_device') as mock_serial:
            # Simulate selecting ports in the combobox
            self.window.qtWindow.comboBox_UART_Laser1.setCurrentIndex(0)
            self.window.qtWindow.comboBox_UART_Laser2.setCurrentIndex(1)
            self.window.qtWindow.comboBox_UART_Robot.setCurrentIndex(2)

            # Call connect_ports
            self.window.connect_ports()

            # Verify port indices are set correctly
            self.assertEqual(self.window.ls_1_port_idx, 0)
            self.assertEqual(self.window.ls_2_port_idx, 1)
            self.assertEqual(self.window.rt_port_idx, 2)

            # Verify serial devices were created with correct parameters
            mock_serial.assert_any_call(
                port_name=self.window.LASER_1_PORT, 
                baudrate=LASER_BAUD_RATE
            )
            mock_serial.assert_any_call(
                port_name=self.window.ROBOT_PORT, 
                baudrate=ROBOT_BAUD_RATE
            )

    def test_import_gcode(self):
        """Test the import_gcode method"""
        # Mock QFileDialog to return a predefined file path
        with patch('PyQt5.QtWidgets.QFileDialog.getOpenFileName', 
                   return_value=('test_file.gcode', '')):
            # Mock the gcode_parser
            with patch('main.gcode_parser.gcode_parser', 
                       return_value=['G1 X10 Y20', 'M4', 'M5']) as mock_parser:
                
                # Call import_gcode
                self.window.import_gcode()

                # Verify file path is displayed
                self.assertIn('test_file.gcode', 
                    self.window.qtWindow.label_imported_gcode.text())

                # Verify gcode lines are parsed
                self.assertIsNotNone(self.window.gcode_line)
                mock_parser.assert_called_once_with('test_file.gcode')

                # Verify start button is enabled
                self.assertTrue(self.window.qtWindow.pushButton_start.isEnabled())

    def test_getAngle(self):
        """Test the getAngle method"""
        # Mock random to provide consistent test results
        with patch('main.random.randint', return_value=250):
            angle = self.window.getAngle()

            # Verify angle is calculated and displayed
            self.assertIsInstance(angle, float)
            self.assertEqual(
                self.window.qtWindow.label_angle.text(), 
                str(angle)
            )

    def test_run_gcode_start_stop(self):
        """Test the run_gcode method for starting and stopping"""
        # Prepare by importing a mock gcode
        self.window.gcode_line = ['M4', 'M0', 'M5']
        
        with patch('main.serial_device') as mock_serial:
        # First call (start)
            self.window.run_gcode()
            self.assertFalse(self.window.isStarting)
            self.assertEqual(
                self.window.qtWindow.pushButton_start.text(), 
                "Stop"
            )
            self.assertFalse(
                self.window.qtWindow.pushButton_import_GCODE.isEnabled()
            )

            # Second call (stop)
            self.window.run_gcode()
            self.assertTrue(self.window.isStarting)
            self.assertEqual(
                self.window.qtWindow.pushButton_start.text(), 
                "Start"
            )
            self.assertTrue(
                self.window.qtWindow.pushButton_import_GCODE.isEnabled()
            )

    def test_data_handler_methods(self):
        """Test the data handler methods"""
        # Create a mock queue
        mock_queue = MagicMock()
        mock_queue.get.return_value = "test_data"

        # Simulate a data handler call
        self.window.LASER_1_ser = MagicMock()
        self.window.LASER_1_ser.queue = mock_queue

        # Call the data handler
        self.window.LASER_1_data_handler()

        # Verify data was put into the queue
        self.assertFalse(self.window.LASER_1_data_queue.empty())
        self.assertEqual(
            self.window.LASER_1_data_queue.get(), 
            "test_data"
        )

    def test_calibration_methods(self):
        """Test the calibration methods"""
        # Mock QTimer.singleShot
        with patch('main.QTimer.singleShot') as mock_single_shot:
            # Call calibration
            self.window.calibration()

            # Verify UI updates
            self.assertEqual(
                self.window.qtWindow.label_Status.text(), 
                "Waiting for calibration ..."
            )
            self.assertFalse(
                self.window.qtWindow.pushButton_UART_connect.isEnabled()
            )

            # Simulate calibration finish
            self.window.calibration_finish()

            # Verify UI updates after calibration
            self.assertEqual(
                self.window.qtWindow.label_Status.text(), 
                "Calibration was completed!"
            )
            self.assertTrue(
                self.window.qtWindow.pushButton_UART_connect.isEnabled()
            )
            self.assertTrue(
                self.window.qtWindow.pushButton_import_GCODE.isEnabled()
            )

if __name__ == '__main__':
    unittest.main()