# This is in early development! 
# Not recommended for use in a production environment.

<br>

# factorio-manager-backend

The backend server which connects your Factorio server to the factorio-manager-frontend web interface or the cli client via TCP Socket.


### Usage:

    python3 factorio-manager-backend.py [options]
- '--help' or '-h' - Show help message and exit.
- '--version' or '-v' - Show program's version number and exit.
- '--config' or '-c' - Specify a config file to use.
- '--log' or '-l' - Specify a log file to use. If not specified, the log will be printed to stdout until '--setup' or '-s' is run, then it will be written to the log file specified in the config file.
- '--log-level' or '-L' - Specify the log level. Default is 'INFO'. Options are 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
- '--setup' or '-s' - Run the first time setup wizard. If specified with '--config' or '-c', the config file will be created at the specified path. Default path is './' Default config file name is 'settings.conf
- '--run' or '-r' - Run the server. If specified with '--config' or '-c', the config file will be loaded from the specified path. Default path and file are './settings.conf'
<br>
<br>

#### Non-Standard Libraries used:

A special thanks to the contributors of these libraries!

- [factorio-rcon-py](https://github.com/mark9064/factorio-rcon-py)
  - License: LGPLv2.1 
  - Usage: Imported directly into the project.
- [factorio-updater](https://github.com/narc0tiq/factorio-updater)
  - License: MIT 
  - Usage: Integrated and modified to work with the project.
