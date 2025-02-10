import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        val = input("Enter your value: ")
        val_b = val.encode('ascii')
        s.sendall(val_b)
        data = s.recv(1024)
        print('Received', repr(data))
