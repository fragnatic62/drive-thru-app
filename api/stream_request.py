import socket

HOST = '192.168.1.107'  # The server's hostname or IP address
PORT = 8000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
