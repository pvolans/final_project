#!/usr/bin/env python

"""gcode_parser.py: gcode_parser description takes GCODE file path and convert it into list.

    This function takes the file name which is inside of GCODE folder as a parameter and convert each line of
    meaningful GCODE command into list.

    An example is given below.    
"""

import os

def parse_gcode(file_name):
    # Define relative path to GCODE folder
    gcode_folder = "GCODE"
    file_path = os.path.join(gcode_folder, file_name)
    gcode_data = []

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found in '{gcode_folder}/' directory.")
        return

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(";"):  # Skip empty lines and comments
                continue

            parsed_line = line.split(";")[0].strip()
            if not parsed_line:
                continue

            if parsed_line:  # Only print if valid
                print(parsed_line)
                gcode_data.append(parsed_line)

    return gcode_data


# Example usage
gcode_data = parse_gcode("sampling_by_3D_printer.gcode")  
print(gcode_data[114])




