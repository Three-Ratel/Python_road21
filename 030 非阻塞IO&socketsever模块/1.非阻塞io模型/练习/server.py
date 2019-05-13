#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socket
from socket import SOL_SOCKET, SO_REUSEADDR

sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)
sk.listen()

user = []
del_user = []
while True:
    try:
        con, addr = sk.accept()
        user.append((con, addr))
    except BlockingIOError:
        for i in user:
            print(i[1])
            time.sleep(1)
            try:
                print('>>>>>>>>>>>>>>>>>')
                msg = i[0].recv(1024).decode('utf-8')
                print('----------------')
                print('~~~~~~~~~~~~~~', msg)
                if not msg:
                    # del_user.app
                    # end(i)
                    continue
                i[0].send(msg.upper().encode('utf-8'))
            except Exception as e:print(e)
        for i in del_user:
            user.remove(i)
        del_user.clear()

sk.close()
