import socket

if __name__ == '__main__':
    host = '192.168.1.56'
    port = 4444
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))
    client.send(b'TCP connection established')

    received_data = client.recv(4096)
    print(f'Server`s data: {received_data.decode()}')

    client.close()
