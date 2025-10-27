import time
import socket
import numpy as np

HOST='127.0.0.1'
PORT=5000

def tcp_thread():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        print("attempting to connect")
        conn, addr = s.accept()
        is_connected = True
        try:
            while True:
                final_dict = np.zeros((55,)).tobytes()
                conn.sendall(final_dict)
                time.sleep(0.2)
        except (BrokenPipeError, ConnectionResetError):
            print("client disconnected")
            is_connected = False
            continue

tcp_thread()