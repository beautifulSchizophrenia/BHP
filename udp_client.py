import socket

if __name__ == '__main__':
    host = '192.168.1.56'
    port = 4444
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp.sendto(b'UDP connection established', (host, port))
    data, addr = udp.recvfrom(4096)

    print(f' Received Data: {data.decode()}')
    udp.close()
