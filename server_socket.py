import socket
import utilities


def create_socket_listener():
    # Create a socket object
    s = socket.socket()
    ip_address = utilities.server_settings['ip_address']
    port_number = utilities.server_settings['port_number']
    # Bind to the port
    s.bind((ip_address, port_number))

    # Put the socket into listening mode
    s.listen(5)
    print("Socket is listening")

    # A forever loop until we interrupt it or an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        # If we are restricting clients and the client address is not in allowed_clients, close the connection
        if utilities.server_settings['allowed_clients'] != '*' and \
                addr[0] not in utilities.server_settings['allowed_clients']:
            print(f'Client address {addr[0]} is not in allowed_clients')
            c.close()
            continue
        # send a thank-you message to the client.
        c.send(b'Thank you for connecting')
        # Close the connection with the client
        c.close()
