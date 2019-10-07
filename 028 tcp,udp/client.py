# client 端
from socket import socket
sk = socket()
sk.connect(("127.0.0.1", 8001))
sk.send(b'hello')
msg = sk.recv(1024)
print(msg)
sk.close()