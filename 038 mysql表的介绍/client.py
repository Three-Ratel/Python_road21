#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from socket import socket
sk = socket()
sk.connect(('127.0.0.1', 9000))
while True:
    sk.send('hello'.encode('utf-8'))
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    time.sleep(0.1)


