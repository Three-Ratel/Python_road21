#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.connect(('192.168.12.62', 9000))
msg = sk.recv(1024).decode('utf-8')
print(msg)

# sk.send(b'byebye')


content = input('请输入内容：').encode('utf-8')
sk.send(content)
