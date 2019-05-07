#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))

n = sk.listen()


i = 31
while True:
    con, add = sk.accept()
    while True:
        data = con.recv(1024).decode('utf-8')
        if data.upper() == 'Q':
            break
        print('\033[%sm%s\033[0m' % (i, data))

        data = input('请输入内容：')
        con.send(data.encode('utf-8'))
        if data.upper() == 'Q': break

    con.close()
    i += 1
    if i == 38:
        i = 31



sk.close()



