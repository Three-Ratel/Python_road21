#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
sk = socket.socket()
sk.bind(("127.0.0.1", 8000))
sk.listen(5)
conn, addr = sk.accept()
msg = conn.recv(1024)
print(msg)
conn.send(b"HTTP/1.1 200 OK \r\n")
conn.send("你好".encode("utf-8"))