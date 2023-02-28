import utilities
from twisted.internet import protocol, reactor
import json
import server_commands


class ListenAndReply(protocol.Protocol):
    def dataReceived(self, data):
        client_ip = str(self.transport.getHost().host)
        print(f'Received connection from {client_ip}')
        # If we are restricting clients and the client address is not in allowed_clients, close the connection
        if utilities.server_settings(file_path='settings.conf')['allowed_clients'] != '*' and \
                client_ip not in utilities.server_settings(file_path='settings.conf')['allowed_clients']:
            print(f'Client address {client_ip} is not in allowed_clients')
            self.transport.loseConnection()
            return
        command_result = server_commands.parse(utilities.bytes_to_string(data))
        self.transport.write(utilities.string_to_bytes(command_result))


def start():
    factory = protocol.ServerFactory()
    factory.protocol = ListenAndReply
    reactor.listenTCP(utilities.server_settings(file_path='settings.conf')
                      ['backend_server_manager_listen_port'], factory)
    reactor.run()