#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
con, add = sk.accept()
con.send(b'hello')

data = con.recv(1024).decode('utf-8')
print(data)

con.close()
sk.close()



