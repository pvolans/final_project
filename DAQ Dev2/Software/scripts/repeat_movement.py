import serial
import time

# Configure your serial port and baud rate (default GRBL is 115200)
SERIAL_PORT = 'COM12'  # Replace with your port, e.g. '/dev/ttyUSB0' on Linux/Mac
BAUD_RATE = 115200

def send_gcode(ser, command):
    full_command = command.strip() + '\n'
    ser.write(full_command.encode())
    print(f">> Sent: {command}")
    time.sleep(0.1)  # Give GRBL time to process

def wait_for_ok(ser):
    while True:
        line = ser.readline().decode().strip()
        if line == 'ok':
            print("<< Received: ok")
            break
        elif line:
            print(f"<< Received: {line}")

def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            # Wait for GRBL to initialize
            time.sleep(2)
            ser.flushInput()

            # Wake up GRBL
            send_gcode(ser, "\r\n\r\n")
            time.sleep(2)
            ser.flushInput()

            #Homing
            send_gcode(ser, "G28")
            wait_for_ok(ser)

            # Send first command once
            send_gcode(ser, "G0 X0 Y10")
            wait_for_ok(ser)


            # Start loop: alternate between two positions
            while True:
                send_gcode(ser, "G0 X0 Y10")
                wait_for_ok(ser)

                send_gcode(ser, "G0 X25 Y10")
                wait_for_ok(ser)

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
