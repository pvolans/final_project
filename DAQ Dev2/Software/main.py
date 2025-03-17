import serial
import time
import csv
from datetime import datetime
import os

import gcode_parser 

# Configuration
PORT_LASER_1 = '/dev/ttyUSB0'  # Replace with the serial port of 1st M703A laser module
PORT_LASER_2 = '/dev/ttyUSB1'  # Replace with the serial port of 2nd M703A laser module

LASER_BAUD_RATE = 256000
DATA_LIMIT = 4000  # Maximum number of data entries

PORT_ROBOT = '/dev/ttyUSB2' # Replace with the serial port of Cartesian Robot

ROBOT_BAUD_RATE = 115200

def main():

    # Open serial port for LASER_1, LASER_2 and Cartesian Robot
    with serial.Serial(PORT_LASER_1, LASER_BAUD_RATE, timeout=1) as LASER_1_ser, \
         serial.Serial(PORT_LASER_2, LASER_BAUD_RATE, timeout=1) as LASER_2_ser, \
         serial.Serial(PORT_ROBOT, ROBOT_BAUD_RATE, timeout=1) as ROBOT_ser:
        
        print(f"Connected to {PORT_LASER_1} at {LASER_BAUD_RATE} baud.")
        print(f"Connected to {PORT_LASER_2} at {LASER_BAUD_RATE} baud.")
        print(f"Connected to {PORT_ROBOT} at {ROBOT_BAUD_RATE} baud.")

        # Send "E" to the module
        LASER_1_ser.write(b'E')
        LASER_2_ser.write(b'E')

        print("Sent 'E' command to the modules.")

        print("Press 'S' to start the sampling process.")
        
        while True:
            user_input = input("Enter: ").strip().upper()
            
            if user_input == "S":
                print("Code started!")
                LASER_1_ser.write(b'C')
                print(f"Waiting for calibration [LASER_1]...")
                time.sleep(13)
                LASER_1_ser.write(b'E')

                break
            else:
                print("Invalid input. Please press 'S' to start.")

        point = 0
        sample = 0
        data_entries = []

        while True:

            ser.write(b'E')
            print("Sent 'E' command to the module.")
            print("Collecting APD data with Laser...")
            while len(data_entries) < DATA_LIMIT:
                if ser.in_waiting:
                    # Read a line of incoming data
                    line = ser.readline().decode('utf-8').strip()
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            # Split the line and extract numerical values
                    parts = line.split(';')
                    numerical_values = [parts[i].replace('[', '').replace(']', '') for i in range(1, len(parts), 2)]
                    data_entries.append(numerical_values + [timestamp])

       
            # Save data to a CSV file
            file_name = f"data_{sample_numbers[sample]}_{point}_L.csv"
    
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["DIST", "AMP", "TEMP", "VOLT","Timestamp"])
                writer.writerows(data_entries)
            print(f"Saved {len(data_entries)} entries to {file_name}.")
            data_entries = []

            ser.write(b'L')
            print("Sent 'L' command to the module.")
            print("Collecting APD data without Laser...")
            while len(data_entries) < DATA_LIMIT:
                if ser.in_waiting:
                    # Read a line of incoming data
                    line = ser.readline().decode('utf-8').strip()
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            # Split the line and extract numerical values
                    parts = line.split(';')
                    numerical_values = [parts[i].replace('[', '').replace(']', '') for i in range(1, len(parts), 2)]
                    data_entries.append(numerical_values + [timestamp])
            
            # Save data to a CSV file
            file_name = f"data_{sample_numbers[sample]}_{point}.csv"      
                  
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["DIST", "AMP", "TEMP", "VOLT","Timestamp"])
                writer.writerows(data_entries)

            print(f"Saved {len(data_entries)} entries to {file_name}.")
            data_entries = []
            if point < 36:
                point = point + 1
                wait_time = WAIT_TIME_TWO_POINT
            else:
                point = 0
                wait_time = WAIT_TIME_TWO_SAMPLE
                sample = sample + 1

            if (sample + 1) % 3 == 0:
                wait_time = WAIT_TIME_NEXT_COLUMN
            if sample == 9:
                print("Finished succesfully!")
                break
            # Wait before the next iteration
            print(f"Waiting for {wait_time} seconds...")
            time.sleep(wait_time)


if __name__ == "__main__":
    main()
