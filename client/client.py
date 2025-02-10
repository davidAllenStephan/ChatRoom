import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def send_data(s):
    while True:
        val = input()
        val_b = val.encode('ascii')
        s.sendall(val_b)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
t = threading.Thread(target=send_data, args=(s,))
t.start()
while True:
    data = s.recv(1024)
    data_s = data.decode('utf-8')
    print(data_s)
