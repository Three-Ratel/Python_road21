#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
使用TCP协议发送数据为空时，默认不会发送
"""
import os
import socket
import hmac


def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        print('------>', msg)
        con.send(msg.upper().encode('utf-8'))
        # con.send(''.encode('utf-8'))


sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

com_key = b'henry'
while True:
    con, addr = sk.accept()
    sec_key = os.urandom(32)
    con.send(sec_key)          # 第一次发送
    val = hmac.new(com_key, sec_key).digest()
    data = con.recv(32)   # 第一次接收
    if data == val:
        print('客户端合法')
        print(con, addr)
        chat(con)
    else:
        print('客户端不合法')
        con.close()
sk.close()




