#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.sendto('%Y-%m-%d'.encode('utf-8'), (('127.0.0.1', 9000)))
time, addr = sk.recvfrom(1024)
print(time.decode('utf-8'))
sk.close()




