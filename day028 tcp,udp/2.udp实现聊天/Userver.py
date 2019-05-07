#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

i = 31
info = {}
while True:
    msg, client_addr = sk.recvfrom(1024)
    msg = msg.decode('utf-8')

    flag = msg.split(': ')
    if flag[1].strip().upper() == 'Q':
        info.pop(flag[0])
        continue

    if info.get(flag[0]): pass
    else:
        i += 1
        if i == 38: i = 31
        info[flag[0]] = i
    print(info)
    c = info[flag[0]]
    print('\033[%sm%s\033[0m' % (c, msg,))

    data = input('>>>')
    sk.sendto(data.encode('utf-8'), client_addr)
    if data.strip().upper() == 'Q': break


sk.close()



