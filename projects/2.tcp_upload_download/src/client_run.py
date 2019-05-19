#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, socket
# PRO_DIR = os.path.dirname(os.path.dirname(__file__))
PRO_DIR = '/Users/henry/programme/python/Python_codes/projects/2.tcp_upload_download'
sys.path.append(PRO_DIR)
from bin import client
from config import settings


def run():
    sk = socket.socket()
    sk.connect(settings.IP_PORT)
    obj = client.Client(sk)
    user = client.User(obj)
    print("""
            1.用户注册 2.用户登陆 
            download file_name / upload file_name
            ls / cd / cd.. / mkdir
            """)

    while True:

        choice = input('>>>').strip()
        if choice.upper() == 'Q':
            obj.qu_fun('Q')
            return
        if choice == '1':
            user.register()
        elif choice == '2':
            user.login()
        else:
            if ' ' not in choice:
                choice = choice + ' '
            choice = choice.split(' ')
            try:
                if choice[0] == 'cd..':choice[0] = 'cd_up'
                if hasattr(obj, choice[0]): getattr(obj, choice[0])(choice[1])
            except BrokenPipeError:
                sk.close()
                sk = socket.socket()
                sk.connect(settings.IP_PORT)
                obj = client.Client(sk)
                user = client.User(obj)
                print('请登陆后使用')


run()
