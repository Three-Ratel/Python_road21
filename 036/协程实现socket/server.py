#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import socket
import gevent
from gevent import monkey
from gevent import socket

monkey.patch_all()

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()


def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        con.send(msg.upper().encode('utf-8'))


while True:
    con, _ = sk.accept()
    gevent.spawn(chat, con)
