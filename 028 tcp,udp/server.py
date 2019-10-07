# server 端
from socket import socket

sk = socket()
sk.bind(("127.0.0.1", 8000))
sk.listen()
conn, addr = sk.accept()
msg = conn.recv(1024)
print(msg)
conn.send(msg.decode('utf8').upper().encode('utf8'))
conn.close()
sk.close()

