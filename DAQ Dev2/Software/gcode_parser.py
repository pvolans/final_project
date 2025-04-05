#!/usr/bin/env python

"""gcode_parser.py: gcode_parser description takes GCODE file path and convert it into list.

    This function takes the file name which is inside of GCODE folder as a parameter and convert each line of
    meaningful GCODE command into list.

    An example is given below.  

    # Example usage
    gcode_data = gcode_parser("sampling_by_3D_printer.gcode")  
    print(gcode_data[114])  
"""

import os

def gcode_parser(file_name):
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

            parsed_line = line.split(";")[0].strip() # Add only GCODE commands, do not take the element after ";"  
            if not parsed_line:
                continue

            if parsed_line:  # Only print and append if it is valid
                #print(parsed_line)
                gcode_data.append(parsed_line)

    return gcode_data







