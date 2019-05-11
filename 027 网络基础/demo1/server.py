#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))

n = sk.listen()
while True:
    con, add = sk.accept()
    while True:
        data = con.recv(1024).decode('utf-8')
        if data.upper() == 'Q':
            break
        print(data)

        content = input('请输入内容：')
        con.send(content.encode('utf-8'))
        if content.upper() == 'Q': break

    con.close()

sk.close()



