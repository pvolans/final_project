import os

def gcode_parser(file_name):
    # Define relative path to GCODE folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gcode_folder = os.path.join(base_dir, "GCODE")
    file_path = os.path.join(gcode_folder, file_name)
    gcode_data = []

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found in '{gcode_folder}/' directory.")
        return None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(";"):  # Skip empty lines and comments
                continue

            parsed_line = line.split(";")[0].strip() # Add only GCODE commands, do not take the element after ";"  
            if not parsed_line:
                continue

            if parsed_line:  # Only append if it is valid
                gcode_data.append(parsed_line)

    return gcode_data