#!/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import socket
sk = socket()
sk.connect(('127.0.0.1', 9000))
while True:
    data = input('>>>')
    sk.send(data.encode('utf-8'))
    content = sk.recv(1024).decode('utf-8')
    print(content)

sk.close()




