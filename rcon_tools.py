import factorio_rcon
import sys
import utilities


def rcon_client() -> 'factorio_rcon.RCONClient':
    try:
        host = utilities.server_settings(file_path='settings.conf')['factorio_rcon_host']
        port = utilities.server_settings(file_path='settings.conf')['factorio_rcon_port']
        password = utilities.server_settings(file_path='settings.conf')['factorio_rcon_password']
        client = factorio_rcon.RCONClient(host, port, password)
        return client
    except Exception as e:
        print(f'Caught an unexpected exception creating the RCON client: {e}')
        print(f'Now exiting')
        sys.exit(1)


def send_rcon_command(command) -> 'command response':
    try:
        client = rcon_client()
        response = client.send_command(command)
        return response
    except Exception as e:
        print(f'Caught an unexpected exception sending the RCON command: {e}')
        print(f'Now exiting')
        sys.exit(1)


def list_commands() -> 'string of commands':
    return send_rcon_command('/h')


def shout_message(message) -> 'returns None when successful':
    return send_rcon_command(message)


def list_players() -> 'string of players - online is denoted with "(online)"':
    return send_rcon_command('/players')


def list_admins() -> 'string of admins - online is denoted with "(online)"':
    return send_rcon_command('/admins')
