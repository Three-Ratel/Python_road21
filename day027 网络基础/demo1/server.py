#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))

sk.listen()

con, add = sk.accept()

while True:
    content = input('请输入内容：')
    con.send(content.encode('utf-8'))
    if content.upper() == 'Q': break

    data = con.recv(1024).decode('utf-8')
    if data == 'Q':
        break
    print(data)


con.close()
sk.close()



