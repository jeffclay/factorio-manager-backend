# Description: This file is used to gather required settings and populate the settings.conf file.

import logging
import time
import socket
import os
import utilities
from pathlib import Path

logger = logging.getLogger(__name__)
logging.info('Starting the setup process.')


def prompt_for_settings() -> 'dictionary of settings':
    # Prompt for each setting separately and store them in a dictionary
    settings_dict = dict()
    utilities.clear()
    print('Welcome to the Factorio Backend Server Manager setup wizard.')
    print('This wizard will guide you through the process of setting up the server manager.')
    print('Please note that this wizard will not configure the Factorio server.')
    print('You will need to configure the Factorio server separately.')
    print('Press enter to continue.')
    input()
    utilities.clear()
    print('If this is blank, the default port 4192 will be used.')
    settings_dict['backend_server_manager_listen_port'] = \
        input('Enter the port that this server manager will listen on: ')

    utilities.clear()
    print('If this is blank, we will attempt to bind to 0.0.0.0')
    settings_dict['backend_server_manager_listen_ip'] = \
        input('Enter the IP address that this server manager will listen on: ')

    utilities.clear()
    print('This must be provided.')
    settings_dict['factorio_rcon_host'] = input('Enter the IP address or host in which the'
                                                ' Factorio RCON service is listening: ')

    utilities.clear()
    print('If this is blank, the default port 35198 will be used.')
    settings_dict['factorio_rcon_port'] = input('Enter the port that the Factorio RCON service is listening: ')

    utilities.clear()
    print('This must be provided.')
    settings_dict['factorio_rcon_password'] = input('Enter the password for the Factorio RCON service: ')

    utilities.clear()
    print('If this is blank, the insecure default is to allow connections from any IP address.')
    settings_dict['allowed_clients'] = input('Enter the IP addresses of the clients that are allowed'
                                             ' to connect to this server manager: ', )

    utilities.clear()
    print('This should be the path to the Factorio server executable including the executable name.')
    print('Example: /srv/factorio/bin/x64/factorio')
    settings_dict['factorio_server_path'] = input('Enter the path to the Factorio server executable: ')

    utilities.clear()
    print('This should be only the path where you want to save the settings.conf file needed for this server manager.')
    settings_dict['settings_file_location'] = input('Enter the path where we should store the settings.conf file: ')

    utilities.clear()
    print('This should be only the path where you want to save the log files.')
    settings_dict['log_file_location'] = input('Enter the path where we should store the log files: ')

    return settings_dict


def validate_settings(settings_dict) -> bool:
    # Validate the settings provided from prompt_for_settings()
    if not settings_dict['backend_server_manager_listen_port'].isdigit():
        logger.error('The backend_server_manager_listen_port is not a number.')
        return False
    if not settings_dict['factorio_rcon_port'].isdigit():
        logger.error('The factorio_rcon_port is not a number.')
        return False
    if not os.path.exists(settings_dict['factorio_server_path']):
        logger.error('The factorio_server_path does not exist.')
        return False
    if os.path.isdir(settings_dict['factorio_server_path']):
        logger.error('The factorio_server_path is a directory, not a file.')
        return False
    if settings_dict['factorio_server_path'].endswith('factorio.exe'):
        logger.warning('None of this has been tested with Windows. You may have issues!')
        print('None of this has been tested with Windows. You may have issues!')
        print('Press Ctrl+C to cancel or wait 5 seconds to continue.')
        time.sleep(5)
    if settings_dict['settings_file_location'].endswith('settings.conf'):
        logger.warning('The settings_file_location should be a directory, not a file.')
        return False
    if not os.path.exists(settings_dict['settings_file_location']):
        logger.error('The settings_file_location does not exist.')
        return False
    if not os.path.isdir(settings_dict['settings_file_location']):
        logger.error('The settings_file_location is not a directory.')
        return False
    # Socket connection test to the Factorio RCON service
    if not attempt_socket_connection(settings_dict['factorio_rcon_host'], settings_dict['factorio_rcon_port']):
        logger.error(f'Unable to connect to the Factorio RCON service using: {settings_dict["factorio_rcon_host"]} '
                     f'at port {settings_dict["factorio_rcon_port"]}')
        return False
    # Socket connection test to the backend_server_manager_listen_port is available.
    if attempt_socket_connection(settings_dict['backend_server_manager_listen_ip'],
                                 settings_dict['backend_server_manager_listen_port']):
        logger.error(f'The port {settings_dict["backend_server_manager_listen_port"]} is already in use.')
        return False
    if not os.path.exists(settings_dict['log_file_location']):
        logger.error('The log_file_location does not exist.')
        return False
    if not os.path.isdir(settings_dict['log_file_location']):
        logger.error('The log_file_location is not a directory.')
        return False
    if not Path(settings_dict['log_file_location'] + '/factorio_manager').mkdir():
        logger.error('Unable to create the log file directory.')
        return False
    return True


def attempt_socket_connection(host, port) -> bool:
    # Attempt to connect to the socket and return True or False
    # This is used to test the connection to the Factorio RCON service
    # This is also used to confirm that our listen port is not already in use
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp_socket.settimeout(2)
        temp_socket.connect((host, port))
        temp_socket.close()
        return True
    except Exception as e:
        logger.info(f'Unable to establish a connection to {host} at port {port}. Error: {e}')
        logger.info('If we are checking for a port in use, this is expected. If we are checking for a connection'
                    ' to the Factorio RCON service, this is not expected.')
        return False



