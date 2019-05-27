#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""tcp client"""
import time
from socket import socket

sk = socket()
sk.connect(('127.0.0.1', 9000))
count = 0
while True:
    count += 1
    sk.send('hello'.encode('utf-8'))
    msg = sk.recv(1024).decode('utf-8')
    print(msg, count)
    time.sleep(0.1)

# import time
# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
# while True:
#     data = 'hello'.encode('utf-8')
#     sk.sendto(data, ('127.0.0.1', 9000))
#     msg, addr = sk.recvfrom(1024)
#     msg.decode('utf8')
#     print(msg)
#     time.sleep(0.1)
