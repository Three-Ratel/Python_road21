#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import pickle
import struct
import hashlib
from socketserver import *
from lib import get_md5, get_dir_size
from config import settings

VIP_L = set()


class User(object):
    def __init__(self, obj):
        self.obj = obj

    def login(self):
        while True:
            dic = self.obj.my_recv()
            if dic['user_name'] == 'Q': return
            flag = False
            with open(settings.USER_INFO, 'rb') as f:
                try:
                    while True:
                        user_dic = pickle.load(f)
                        if dic['user_name'] == user_dic['user_name'] and get_md5.get_md5(dic) == user_dic['user_pwd']:
                            flag = True
                            settings.USER_DIR = os.path.join(settings.SER_DIR, user_dic['user_name'])
                            if user_dic['ident'] == 'vip':
                                VIP_L.add(user_dic['user_name'])
                            break
                except:pass

            dic = {'operator': flag}
            self.obj.my_send(dic)
            if flag: return flag

    def register(self):
        dic = self.obj.my_recv()
        flag = True
        with open(settings.USER_INFO, 'rb') as f:
            try:
                while True:
                    user_dic = pickle.load(f)
                    if dic['user_name'] == user_dic['user_name']:
                        flag = False
            except:pass

        if not flag:
            """用户名已存在"""
            status_dic = {'operator': flag}
            self.obj.my_send(status_dic)
        else:
            """把用户名、密码和身份信息写入user_info文件"""
            with open(settings.USER_INFO, 'ab') as f:
                pickle.dump({'user_name': dic['user_name'],
                             'user_pwd': get_md5.get_md5(dic), 'ident': 'ordinary'}, f)
                settings.USER_DIR = os.path.join(settings.SER_DIR, dic['user_name'])
                if not os.path.exists(settings.USER_DIR): os.makedirs(settings.USER_DIR)
                status_dic = {'operator': flag}
                self.obj.my_send(status_dic)


class Myserver(BaseRequestHandler):

    def my_recv(self, encoding='utf-8'):
        """第一次接收报文头"""
        len_dic = self.request.recv(4)
        len_dic = struct.unpack('i', len_dic)[0]
        str_dic = self.request.recv(len_dic).decode(encoding)
        dic = json.loads(str_dic)
        return dic

    def my_send(self, dic, encoding='utf-8'):
        """发送报文头"""
        byte_dic = json.dumps(dic).encode(encoding)
        len_dic = struct.pack('i', len(byte_dic))
        self.request.send(len_dic)
        self.request.send(byte_dic)

    def file_send(self, dic):
        file_path = os.path.join(settings.USER_DIR, dic['file_name'])
        dic = {}
        if not os.path.isfile(file_path):
            dic['isfile'] = False
        else:
            dic['isfile'] = True
            file_size = os.path.getsize(file_path)
            dic['file_size'] = file_size
        self.my_send(dic)
        if not dic['isfile']: return
        obj = hashlib.md5()
        with open(file_path, mode='rb') as f:
            while dic['file_size']:
                content = f.read(2048)
                self.request.send(content)
                dic['file_size'] -= len(content)
                """校验文件"""
                obj.update(content)
        """发送文件的 md5 值"""
        self.request.send(obj.hexdigest().encode('utf-8'))

    def file_recv(self, dic):

        def inner(buffer_size=2048, buffer=2048):
            while dic['file_size'] > buffer_size:
                content = self.request.recv(buffer)
                f.write(content)
                dic['file_size'] -= len(content)
                """校验文件"""
                obj.update(content)

        obj = hashlib.md5()
        user_size = get_dir_size.get_dir_size(settings.USER_DIR)

        name = os.path.basename(settings.USER_DIR)
        if name in VIP_L:
            size = settings.VIP_SIZE
        else:
            size = settings.DIR_SIZE

        flag = True
        if user_size + dic['file_size'] <= size:
            state_dic = {'operator': flag}
            self.my_send(state_dic)

            file_path = os.path.join(settings.USER_DIR, dic['file_name'])
            with open(file_path, mode='wb') as f:
                inner()
                inner(0, dic['file_size'])
            """发送文件的 md5 值"""
            self.request.send(obj.hexdigest().encode('utf-8'))
        else:
            flag = False
            state_dic = {'operator': flag}
            self.my_send(state_dic)

    def ls(self, dic):
        user_home = os.listdir(settings.USER_DIR)
        user_home_dic = {'content': user_home}
        self.my_send(user_home_dic)

    def cd(self, dic):
        user_home = os.listdir(settings.USER_DIR)
        flag = False
        settings.USER_DIR = os.path.join(settings.USER_DIR, dic['dir_name'])
        if dic['dir_name'] in user_home and os.path.isdir(settings.USER_DIR):
            flag = True
        status_dic = {'status': flag}
        self.my_send(status_dic)

    def cd_up(self, dic):
        flag = False
        home_name = os.path.basename(settings.USER_DIR)
        settings.USER_DIR = os.path.dirname(settings.USER_DIR)
        if settings.USER_DIR != settings.SER_DIR:
            flag = True
        else:settings.USER_DIR = os.path.join(settings.USER_DIR, home_name)
        status_dic = {'status': flag}
        self.my_send(status_dic)

    def mkdir(self, dic):
        flag = False
        if not os.path.isdir(os.path.join(settings.USER_DIR, dic['dir_name'])):
            flag = True
            os.makedirs(os.path.join(settings.USER_DIR, dic['dir_name']))
        status_dic = {'status': flag}
        self.my_send(status_dic)

    # def rm(self,dic):
    #     if os.path.isdir(os.path.join(settings.USER_DIR, dic['file_name'])):
    #         os.removedirs(os.path.join(settings.USER_DIR, dic['file_name']))
    #     else:os.remove(os.path.join(settings.USER_DIR, dic['file_name']))

    def handle(self):
        while True:
            try:
                dic = self.my_recv()
                if dic['operator'] == 'Q':
                    pass
                elif dic['operator'] == 'login':
                    if User(self).login(): break
                elif dic['operator'] == 'register':
                    User(self).register()
            except:
                return
        while True:
            try:
                dic = self.my_recv()
                if dic['operator'] == 'Q':
                    name = os.path.basename(settings.USER_DIR)
                    VIP_L.discard(name)
                    break
                if hasattr(self, dic['operator']): getattr(self, dic['operator'])(dic)
            except:pass


