#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import struct
import socket

IP_PORT = ('127.0.0.1', 9000)
sk = socket.socket()
sk.connect(IP_PORT)
FILE_PATH = '/Users/henry/programme/python/Python_codes/day030\
 非阻塞IO&socketsever模块/tcp文件上传、下载/db/client_dir'


class Client():

    def my_recv(self, encoding='utf-8'):
        """
        第一次接收报文头
        :return:
        """
        len_dic = sk.recv(4)
        len_dic = struct.unpack('i', len_dic)[0]
        str_dic = sk.recv(len_dic).decode(encoding)
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
        sk.send(len_dic)
        sk.send(byte_dic)

    def file_recv(self, dic, file_name):
        def inner(buffer=2048):
            while dic['file_size'] > buffer:
                content = sk.recv(buffer)
                f.write(content)
                dic['file_size'] -= len(content)
        file_path = os.path.join(FILE_PATH, file_name)
        with open(file_path, mode='wb') as f:
            inner()
            inner(dic['file_size'])

    def file_send(self, dic, file_path):
        with open(file_path, mode='rb') as f:
            while dic['file_size'] > 2048:
                content = f.read(2048)
                sk.send(content)
                dic['file_size'] -= len(content)
            else:
                content = f.read()
                sk.send(content)

    def download(self):
        file_name = input('请输入要下载文件：')
        dic = {'file_name': file_name, 'operation': 'download'}
        self.my_send(dic)
        dic = self.my_recv()
        if dic['isfile']:
            self.file_recv(dic, file_name)
        else:
            print('您下载的文件不存在')

    def upload(self):
        while True:
            file_name = input('请输入要上传文件名：')
            file_path = os.path.join(FILE_PATH, file_name)
            if os.path.isfile(file_path): break
            print('文件不存在,请重新输入')
        file_size = os.path.getsize(file_path)
        dic = {'file_name': file_name, 'file_size': file_size,
               'operation': 'upload'}
        self.my_send(dic)
        self.file_send(dic, file_path)


Client().upload()
