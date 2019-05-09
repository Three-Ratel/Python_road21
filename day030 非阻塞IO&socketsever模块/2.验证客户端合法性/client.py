#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import hashlib


def chat(sk):
    while True:
        sk.send('hello'.encode('utf-8'))
        msg = sk.recv(1024).decode('utf-8')
        print('------>', [msg])


def get_md5(com_key, sec_key):
    md5 = hashlib.md5(com_key)
    md5.update(sec_key)
    return md5.hexdigest()


sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
sec_key = sk.recv(32)      # 第一次接收
com_key = b'henry'
val = get_md5(com_key, sec_key)

sk.send(val.encode('utf-8)'))             # 第一次发送
chat(sk)


sk.close()




