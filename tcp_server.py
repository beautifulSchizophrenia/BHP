import socket
import threading


def client_handler(client_socket):
    with client_socket as sock:
        client_data = sock.recv(4096)
        print(f'Client`s data: {client_data.decode()}\n')
        sock.send(b'ACK')


if __name__ == '__main__':
    host = '192.168.1.56'
    port = 4444
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))
    server.listen(15)
    print('[+] Server is up\n')

    while True:
        data_socket, address = server.accept()
        print(f'[+] User with IP: {address[0]}:{address[1]} connected\n')

        handler = threading.Thread(target=client_handler, args=(data_socket, ))
        handler.start()
