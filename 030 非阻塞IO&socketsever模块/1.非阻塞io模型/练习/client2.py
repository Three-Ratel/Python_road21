#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    print('-----------------------')
    sk.send('echo'.encode('utf-8'))
    time.sleep(5)
    msg = sk.recv(1024).decode('utf-8')
    print(msg)




