#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, socket
PRO_DIE = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PRO_DIE)
from bin import client
from config import settings

def run():
    sk = socket.socket()
    sk.connect(settings.IP_PORT)
    obj = client.Client(sk)
    user = client.User(obj)
    fun_dic = {'1': user.register, '2': user.login, '3': obj.upload, '4': obj.download}
    while True:
        print("""
            1.用户注册 2.用户登陆 3.上传文件 4.下载文件
            """)
        choice = input('请输入功能选项(Q)：').strip()
        if choice.upper() == 'Q':
            obj.qu_fun('Q')
            return
        if not fun_dic.get(choice): continue
        try:
            fun_dic[choice]()
        except BrokenPipeError:
            sk.close()
            sk = socket.socket()
            sk.connect(settings.IP_PORT)
            obj = client.Client(sk)
            user = client.User(obj)
            print('请登陆后使用')

run()
