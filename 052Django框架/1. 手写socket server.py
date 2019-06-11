#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
from socket import SOL_SOCKET, SO_REUSEADDR
sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8000))
sk.listen(5)
while True:
    con, addr = sk.accept()
    msg = con.recv(1024)
    print(msg)
    con.send(b'HTTP/1.1 200 ok\r\n\r\n')
    con.send(b'<h1>ok<h1>')
    con.close()
sk.close()
