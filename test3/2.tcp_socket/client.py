#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
url = input('>>>')


def my_send(data):
    data = data.encode('utf-8')
    size = struct.pack('i', len(data))
    sk.send(size)
    sk.send(data)


def my_recv():
    size = sk.recv(4)
    size = struct.unpack('i', size)[0]
    return sk.recv(size).decode('utf-8')

my_send(url)
content = my_recv()
print(content)
sk.close()
