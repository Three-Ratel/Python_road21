#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    data = input('>>>').encode('utf-8')
    sk.sendto(data, ('127.0.0.1', 9000))
    if data.decode('utf-8').upper() == 'Q': break

    msg = sk.recv(1024)
    msg = msg.decode('utf-8')
    if msg.upper() == 'Q': break

    print(msg)


sk.close()


