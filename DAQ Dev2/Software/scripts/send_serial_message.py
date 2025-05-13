# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QLabel
from serial_device import serial_device

class SerialGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Serial Sender")
        self.setGeometry(100, 100, 400, 300)

        # Widgets
        self.label = QLabel("Enter message to send:")
        self.line_edit = QLineEdit()
        self.send_button = QPushButton("Send")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.send_button)
        layout.addWidget(self.output)
        self.output.append("Initialisation")
        self.setLayout(layout)
        

        # Serial device setup
        self.ser = serial_device(port_name="COM12", baudrate=115200)  # Change COM3 to your port
        self.ser.data_received.connect(self.display_data)
        self.ser.start()

        # Signals
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.line_edit.text()
        if message:
            self.ser.send(message + '\n')  # Add newline if needed
            self.output.append(f"Sent: {message}")
            self.line_edit.clear()

    def display_data(self, data):
        self.output.append(f"Received: {data}")

    def closeEvent(self, event):
        self.ser.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialGUI()
    window.show()
    sys.exit(app.exec_())
