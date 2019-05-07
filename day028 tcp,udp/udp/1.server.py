#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

while True:
    msg, client_addr = sk.recvfrom(1024)
    msg = msg.decode('utf-8')
    if msg.upper() == 'Q': break
    print(msg)

    data = input('>>>').encode('utf-8')
    sk.sendto(data, client_addr)
    if data.decode('utf-8').upper() == 'Q': break


sk.close()



