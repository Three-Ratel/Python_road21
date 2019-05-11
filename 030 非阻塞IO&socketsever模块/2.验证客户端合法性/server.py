#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
使用TCP协议发送数据为空时，默认不会发送
"""
import os
import socket
import hashlib


def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        print('------>', msg)
        con.send(msg.upper().encode('utf-8'))
        # con.send(''.encode('utf-8'))


def get_md5(com_key, sec_key):
    md5 = hashlib.md5(com_key)
    md5.update(sec_key)
    return md5.hexdigest()

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

com_key = b'henry'
while True:
    con, addr = sk.accept()
    sec_key = os.urandom(32)
    con.send(sec_key)          # 第一次发送
    val = get_md5(com_key, sec_key)
    data = con.recv(32).decode('utf-8')   # 第一次接收
    if data == val:
        print('客户端合法')
        chat(con)
    else:
        print('客户端不合法')
        con.close()
sk.close()




