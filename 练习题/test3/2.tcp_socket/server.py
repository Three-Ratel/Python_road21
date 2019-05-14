#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import struct
import requests

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()


def my_recv():
    size = con.recv(4)
    size = struct.unpack('i', size)[0]
    return con.recv(size).decode('utf-8')


def my_send(data):
    data = data.encode('utf-8')
    size = struct.pack('i', len(data))
    con.send(size)
    con.send(data)


con, addr = sk.accept()
msg = my_recv()

content = requests.get(msg)
my_send(content)
con.close()
sk.close()





