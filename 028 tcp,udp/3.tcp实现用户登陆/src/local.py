#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, sys, os
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
from lib.encipher import encipher


sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    print('******* 欢迎登陆 *******')

    user_name = input('请输入用户名(Q/q)：')
    sk.send(user_name.encode('utf-8'))
    if user_name.strip().upper() == 'Q':
        break

    user_pwd = input('请输入密码：')
    user_pwd = encipher(user_pwd)
    sk.send(user_pwd.encode('utf-8'))

    msg = sk.recv(1024).decode('utf-8')
    if msg == '0':
        print('登陆成功')
        break
    elif msg == '1':
        print('用户名或密码错误，请重新输入\n')
        continue
    elif msg == '2':
        print('网站维护中....\n')
        break





