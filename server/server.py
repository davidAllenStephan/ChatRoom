import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def recieve(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        t1 = threading.Thread(target=recieve, args=(conn,))
        t1.start()
