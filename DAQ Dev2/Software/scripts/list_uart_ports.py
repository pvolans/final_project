import serial.tools.list_ports

def list_uart_ports():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No UART ports found.")
        return 

    return ports
