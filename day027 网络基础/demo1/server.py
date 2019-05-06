#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


sk = socket.socket()
sk.bind(('192.168.12.8', 9000))
sk.listen()
con, add = sk.accept()
con.send(b'hello')
while True:
    data = con.recv(1024).decode('utf-8')
    print(data)


con.close()
sk.close()



