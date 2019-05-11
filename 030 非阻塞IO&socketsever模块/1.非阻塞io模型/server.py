#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)
sk.listen()

user = []
del_user = []
while True:
    try:
        con, addr = sk.accept()
        user.append(con)
    except BlockingIOError:
        for i in user:
            try:
                content = i.recv(1024).decode('utf-8')
                if not content:
                    del_user.append(i)
                    continue
                i.send(content.upper().encode('utf-8'))
            except BlockingIOError:pass

        for i in del_user:
            user.remove(i)
        del_user.clear()

sk.close()





