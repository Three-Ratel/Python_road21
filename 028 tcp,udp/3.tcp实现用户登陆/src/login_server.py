#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket, sys, os
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)
path = os.path.join(path, 'db')
path = os.path.join(path, 'user_list.txt')

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

while True:
    con, addr = sk.accept()
    while True:
        user_name = con.recv(1024).decode('utf-8')
        if user_name.strip().upper() == 'Q':
            break
        user_pwd = con.recv(1024).decode('utf-8')
        try:
            f = open(path, mode='r', encoding='utf-8')
        except:
            print('用户信息已丢失')
            con.send('2'.encode('utf-8'))
            continue

        flag = False
        for i in f:
            name, pwd = i.split(':')
            if name == user_name and pwd == user_pwd:
                flag = True
                con.send('0'.encode('utf-8'))  # 登陆成功
                break
        if flag: break
        else: con.send('1'.encode('utf-8'))  # 用户名或密码错误

    f.close()
    con.close()





