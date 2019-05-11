#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

while True:
    con, addr = sk.accept()
    file_name = con.recv(1024).decode('utf-8')
    con.send(b'Q')
    f = open(file_name, mode='wb')
    while True:
        content = con.recv(1024)
        if not content: break
        f.write(content)
    f.close()
    con.close()


