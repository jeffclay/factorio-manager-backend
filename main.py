#!/usr/bin/env python3

import argparse
import sys
import logging
import fmb_setup

version = '0.0.1-alpha'

parser = argparse.ArgumentParser(description='Factorio Backend Server Manager')
parser.add_argument('--version', '-v', help='Show the version number and exit', action='store_true', dest='version')
parser.add_argument('--config', '-c', help='Path to the config file', action='store_true', default='settings.conf',
                    dest='config_file')
parser.add_argument('--log', '-l', help='Path to the log file', action='store_true', default='server_manager.log',
                    dest='log_file')
parser.add_argument('--log-level', '-L', help='Set the log level. Default is INFO. Valid options are: '
                                              'DEBUG, INFO, WARNING, CRITICAL, ERROR.',
                    action='store_true', default='INFO', dest='log_level')
parser.add_argument('--setup', '-s', help='Run the setup wizard', action='store_true', dest='setup')
parser.add_argument('--run', '-r', help='Run the server manager', action='store_true', dest='run')


def main():
    args = parser.parse_args()
    logger = logging.getLogger(__name__)
    if args.log_level:
        logger.setLevel(args.log_level)
    else:
        logger.setLevel(logging.INFO)
    if args.log_file:
        fmb_log_handler = logging.FileHandler(args.log_file)
    else:
        fmb_log_handler = logging.StreamHandler(sys.stdout)
    fmb_log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fmb_log_handler.setFormatter(fmb_log_format)
    logger.addHandler(fmb_log_handler)

    if args.version:
        print(f'Factorio Backend Server Manager version {version}')
        return 0
    if args.setup:
        logger.info('Running the setup wizard')
        setting_dictionary = fmb_setup.prompt_for_settings()
        if fmb_setup.validate_settings(setting_dictionary):
            fmb_setup.write_settings(setting_dictionary, args.config_file)
        return 0
    if args.run:
        logger.info('Running the server manager')
        return 0

    return 0


if __name__ == '__main__':
    sys.exit(main())
