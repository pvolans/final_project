import serial
import time
import csv
from datetime import datetime
import os

# Configuration
PORT = 'COM7'  # Replace with your serial port
BAUD_RATE = 256000
DATA_LIMIT = 4000  # Maximum number of data entries
WAIT_TIME_TWO_SAMPLE = 2
WAIT_TIME_TWO_POINT = 1.5
WAIT_TIME_NEXT_COLUMN = 18
wait_time = WAIT_TIME_TWO_SAMPLE  # Time in seconds to wait after collection
sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    # Open serial port
    with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser:
        print(f"Connected to {PORT} at {BAUD_RATE} baud.")
        
        # Send "E" to the module
        ser.write(b'E')
        print("Sent 'E' command to the module.")

        print("Press 'S' to start the sampling process.")
        
        while True:
            user_input = input("Enter: ").strip().upper()
            
            if user_input == "S":
                print("Code started!")
                ser.write(b'C')
                print(f"Waiting for calibration...")
                time.sleep(13)
                break
            else:
                print("Invalid input. Please press 'S' to start.")
        point = 0
        sample = 3
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
            file_name = f"wo_movement_test_data_{sample_numbers[sample]}_{point}_L.csv"
    
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
            file_name = f"movement_test_data_{sample_numbers[sample]}_{point}.csv"      
                  
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
