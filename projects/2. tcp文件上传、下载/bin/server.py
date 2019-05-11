#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import pickle
import struct
import hashlib
from socketserver import *
from lib import get_md5
from config import settings


class User():
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

                        if dic['user_name'] == user_dic['user_name'] and \
                                get_md5.get_md5(dic) == user_dic['user_pwd']:
                            flag = True
                            settings.USER.append(user_dic['user_name'])
                            print(settings.USER)
                            break
                except:
                    pass
            dic = {'operator': flag}
            self.obj.my_send(dic)
            if flag: return flag

    def register(self):
        user_dic = self.obj.my_recv()
        with open(settings.USER_INFO, 'ab+') as f:
            pickle.dump({'user_name': user_dic['user_name'],
                         'user_pwd': get_md5.get_md5(user_dic)}, f)
            flag = True
            status_dic = {'operator': flag}
            self.obj.my_send(status_dic)


class Myserver(BaseRequestHandler):

    def my_recv(self, encoding='utf-8'):
        """
        第一次接收报文头
        :return:
        """
        len_dic = self.request.recv(4)
        len_dic = struct.unpack('i', len_dic)[0]
        str_dic = self.request.recv(len_dic).decode(encoding)
        dic = json.loads(str_dic)
        return dic

    def my_send(self, dic, encoding='utf-8'):
        """
        发送报文头
        :param dic:
        :return:
        """
        byte_dic = json.dumps(dic).encode(encoding)
        len_dic = struct.pack('i', len(byte_dic))
        self.request.send(len_dic)
        self.request.send(byte_dic)

    def file_send(self, dic):
        file_path = os.path.join(os.path.join(settings.SER_DIR, settings.USER[0]), dic['file_name'])
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
        obj = hashlib.md5()

        def inner(buffer_size=2048, buffer=2048):
            while dic['file_size'] > buffer_size:
                content = self.request.recv(buffer)
                f.write(content)
                dic['file_size'] -= len(content)
                """校验文件"""
                obj.update(content)
        settings.SER_DIR = os.path.join(settings.SER_DIR, settings.USER[0])
        print(settings.SER_DIR)
        if not os.path.exists(settings.SER_DIR): os.makedirs(settings.SER_DIR)
        file_path = os.path.join(settings.SER_DIR, dic['file_name'])
        with open(file_path, mode='wb') as f:
            inner()
            inner(0, dic['file_size'])
        """发送文件的 md5 值"""
        self.request.send(obj.hexdigest().encode('utf-8'))

    def handle(self):
        while True:
            try:
                dic = self.my_recv()
                if dic['operator'] == 'Q': pass
                elif dic['operator'] == 'login':
                    if User(self).login(): break
                elif dic['operator'] == 'register':
                    User(self).register()
            except:return

        while True:
            try:
                dic = self.my_recv()
                if dic['operator'] == 'Q':
                    settings.USER.pop()
                    break
                elif dic['operator'] == 'download':
                    self.file_send(dic)
                elif dic['operator'] == 'upload':
                    self.file_recv(dic)
            except:pass
