#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
from socketserver import *

IP_PORT = ('127.0.0.1', 9000)
FILE_PATH = '/Users/henry/programme/python/Python_codes/day030\
 非阻塞IO&socketsever模块/tcp文件上传、下载/db/server_dir'


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

    def file_send(self, dic, file_path):
        with open(file_path, mode='rb') as f:
            while dic['file_size'] > 2048:
                content = f.read(1024)
                self.request.send(content)
                dic['file_size'] -= len(content)
            else:
                content = f.read()
                self.request.send(content)

    def file_recv(self, dic):
        def inner(buffer=2048):
            while dic['file_size'] > buffer:
                content = self.request.recv(buffer)
                f.write(content)
                dic['file_size'] -= len(content)

        file_path = os.path.join(FILE_PATH, dic['file_name'])
        with open(file_path, mode='wb') as f:
            inner()
            inner(dic['file_size'])

    def download(self, dic):
        file_path = os.path.join(FILE_PATH, dic['file_name'])
        dic = {}
        if not os.path.isfile(file_path): dic['isfile'] = False
        else:
            dic['isfile'] = True
            file_size = os.path.getsize(file_path)
            dic['file_size'] = file_size
        self.my_send(dic)
        if dic['isfile']: self.file_send(dic, file_path)

    def handle(self):
        dic = self.my_recv()
        if dic['operation'] == 'download':
            self.download(dic)
        elif dic['operation'] == 'upload':
            self.file_recv(dic)


server = ThreadingTCPServer(IP_PORT, Myserver)
server.serve_forever()
