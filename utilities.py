import sys
import os
from subprocess import call


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


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')


def bytes_to_string(bytes_object) -> str:
    # Convert bytes to string
    return bytes_object.decode('utf-8')


def string_to_bytes(string) -> bytes:
    # Convert string to bytes
    return bytes(string, 'utf-8')

