import os
import rcon_tools
import argparse


def parse(socket_input):
    if socket_input == '/help':
        return server_help()
    if socket_input == '/factorio-help':
        return rcon_tools.list_commands()
    if socket_input == '/os-uptime':
        return os.popen('uptime -p').read()[:-1]
    if socket_input == '/shout':
        return rcon_tools.shout_message(socket_input.split()[1])
    if socket_input == '/players':
        return rcon_tools.list_players()
    if socket_input == '/admins':
        return rcon_tools.list_admins()


def server_help():
    return 'Commands:\n' \
           '/help - print this help message\n' \
           '/os-uptime - print the server\'s uptime'




