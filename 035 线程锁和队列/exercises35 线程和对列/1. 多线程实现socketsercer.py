#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread
from socket import socket, SO_REUSEADDR, SOL_SOCKET

sk = socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 9000))
sk.listen()

"""
会有两种报错
"""
def chat(con):
    while True:
        try:
            try:
                msg = con.recv(1024).decode('utf-8')
                con.send(msg.upper().encode('utf-8'))
            except ConnectionResetError:pass
        except BrokenPipeError:pass


while True:
    con, _ = sk.accept()
    t = Thread(target=chat, args=(con,))
    t.start()



