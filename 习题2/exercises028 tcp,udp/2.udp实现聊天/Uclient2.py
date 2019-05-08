#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    while True:
        data = input('>>>')
        if data.strip():
            break
        continue

    if data.strip().upper() == 'Q':
        data = 'echo: ' + data
        sk.sendto(data.encode('utf-8'), ('127.0.0.1', 9000))
        break
    data = 'echo: ' + data
    sk.sendto(data.encode('utf-8'), ('127.0.0.1', 9000))

    msg = sk.recv(1024)
    if msg.decode('utf-8').strip() == 'Q': break
    print(msg.decode('utf-8'))


sk.close()







