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
    data = input('>>>')
    sk.send(data.encode('utf-8'))
    msg = sk.recv(1024).decode('utf-8')
    print(msg, count)
    time.sleep(0.1)
