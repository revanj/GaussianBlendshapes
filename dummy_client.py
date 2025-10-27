import socket
import torch
import io
import numpy as np

HOST = '192.168.1.60'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


buffer = b''
chunk = s.recv(4096)
buffer += chunk

print("length of buffer is", len(buffer))

tensor = np.frombuffer(buffer, dtype=np.float32)
print("Client received tensor:\n", tensor)

s.close()