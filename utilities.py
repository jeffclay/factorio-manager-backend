import sys
import os


def server_settings(file_path) -> 'dictionary of settings':
    # Confirm that the file exists
    if not os.path.exists(file_path):
        print('File does not exist')
        sys.exit(1)

    # Read the file and exclude blank lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()
                 and line[0] != '#'
                 and line[0] != '/'
                 and line[0] != '*' and line[0] != ' ']
        # Create a dictionary from the lines
        settings_dict = {}
        for line in lines:
            key, value = line.split(':')
            # Remove any leading or trailing spaces
            key = key.strip()
            value = value.strip()
            # If value contains ' or ", remove them
            if '\'' in value:
                value = value.replace('\'', '')
            if '"' in value:
                value = value.replace('"', '')
            # Check if the value is a number
            if value.isdigit():
                settings_dict[key] = int(value)
                continue
            settings_dict[key] = value
        return settings_dict
