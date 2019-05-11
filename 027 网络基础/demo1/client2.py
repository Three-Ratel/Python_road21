#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    content = input('请输入内容：')
    sk.send(content.encode('utf-8'))
    if content.upper() == 'Q':
        break

    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':break
    print(msg)



sk.close()



