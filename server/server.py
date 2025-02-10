import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


connected_sockets = []
threads = []


def send_to_all(data, conn_cur):
    for conn in connected_sockets:
        if conn != conn_cur:
            conn.sendall(data)


def recieve(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data_utf = data.decode('utf-8')
        text = f'{addr}: {data_utf}'
        text_b = text.encode('ascii')
        send_to_all(text_b, conn)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    connected_sockets.append(conn)
    print('Connected by', addr)
    t = threading.Thread(target=recieve, args=(conn, addr,))
    threads.append(t)
    t.start()
