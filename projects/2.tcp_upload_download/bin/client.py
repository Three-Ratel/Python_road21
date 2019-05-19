#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import json
import struct
import hashlib
from config import settings


def auth(func):

    def inner(*args):
        if settings.STATUS: func(*args)
        else:print('您还未登陆')
        return
    return inner


class Client():
    def __init__(self, sk):
        self.sk = sk

    def process_bar(self, recv_size, file_size):
        """
        rate: 表示接收或发送文件的百分比，* 的个数总共50
        :param recv_size:
        :param file_size:
        :return:
        """
        rate = round(recv_size / file_size * 100, 3)
        rate_size = int(rate)
        r = '%s\033[36m%s%%\033[0m\r' % ('*' * rate_size, rate)
        sys.stdout.write(r)
        sys.stdout.flush

    def qu_fun(self, choice, opt='operator'):
        """
        判断用户choice信息，如果为 Q 则告知服务端，进行断开连接
        :param choice:
        :return:
        """
        flag = True
        dic = {'%s' % opt: choice.upper()}
        if choice.strip().upper() == 'Q':
            self.my_send(dic)
            flag = False
        return flag

    def my_recv(self, encoding='utf-8'):
        """
        第一次接收报文头
        :return:
        """
        len_dic = self.sk.recv(4)
        len_dic = struct.unpack('i', len_dic)[0]
        str_dic = self.sk.recv(len_dic).decode(encoding)
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
        self.sk.send(len_dic)
        self.sk.send(byte_dic)

    def file_recv(self, dic, file_name):
        obj = hashlib.md5()
        file_size = dic['file_size']

        def inner(recv_size = 0, buffersize=2048, recvsize=2048):
            while dic['file_size'] > buffersize:
                content = self.sk.recv(recvsize)
                f.write(content)
                dic['file_size'] -= len(content)
                recv_size += len(content)
                """校验文件"""
                obj.update(content)
                """实现进度条"""
                self.process_bar(recv_size, file_size)
            return recv_size
        file_path = os.path.join(settings.USER_DIR, file_name)
        with open(file_path, mode='wb') as f:
            recv_size = 0
            inner(inner(), 0, dic['file_size'])
        """接收文件的 md5 值"""
        file_md5 = self.sk.recv(32).decode('utf-8')
        if file_md5 == obj.hexdigest():print('\n文件下载成功')
        else:print('\n文件校验失败，请重新下载')

    def file_send(self, dic, file_path):
        obj = hashlib.md5()
        with open(file_path, mode='rb') as f:
            recv_size, file_size = 0, dic['file_size']
            while dic['file_size']:
                content = f.read(2048)
                obj.update(content)
                self.sk.send(content)
                dic['file_size'] -= len(content)
                recv_size += len(content)
                """进度条打印"""
                self.process_bar(recv_size, file_size)
            o_md5 = self.sk.recv(32).decode('utf-8')
            if o_md5 == obj.hexdigest(): print('\n文件上传成功')
            else:print('\033[31m\n文件上传失败\033[0m')

    @auth
    def ls(self):
        dic = {'operator': 'ls'}
        self.my_send(dic)
        dic = self.my_recv()
        for i in dic['content']:
            print(i)

    @auth
    def cd(self):
        dir_name = input('请输入子目录：').strip()
        dic = {'operator': 'cd', 'dir_name':dir_name}
        self.my_send(dic)
        status_dic = self.my_recv()
        if not status_dic['status']:print('%s不是一个有效的文件夹' % dir_name)

    @auth
    def cd_up(self):
        dic = {'operator': 'cd_up'}
        self.my_send(dic)
        status_dic = self.my_recv()
        if not status_dic['status']: print('已经回到家目录')

    @auth
    def mkdir(self):
        dir_name = input('请输入文件夹名称：').strip()
        dic = {'operator': 'mkdir', 'dir_name': dir_name}
        self.my_send(dic)
        status_dic = self.my_recv()
        if not status_dic['status']:print('文件夹已存在')

    # @auth
    # def rm(self):
    #     file_name = input('请输入文件名：').strip()
    #     dic = {'operator': 'rm', 'file_name': file_name}
    #     self.my_send(dic)



    @auth
    def download(self):
        file_name = input('请输入要下载文件(Q)：')
        if file_name.upper() == 'Q': return
        dic = {'file_name': file_name, 'operator': 'file_send'}
        self.my_send(dic)
        dic = self.my_recv()
        if dic['isfile']:self.file_recv(dic, file_name)
        else:print('您下载的文件不存在')

    @auth
    def upload(self):
        while True:
            file_name = input('请输入要上传文件名(Q)：')
            if file_name.upper() == 'Q': return
            file_path = os.path.join(settings.USER_DIR, file_name)
            if os.path.isfile(file_path): break
            print('文件不存在,请重新输入')
        file_size = os.path.getsize(file_path)
        dic = {'file_name': file_name, 'file_size': file_size, 'operator': 'file_recv'}
        self.my_send(dic)
        state_dic = self.my_recv()
        if state_dic['operator']:
            self.file_send(dic, file_path)
        else:print('您的存储空间已不足，请购买VIP')


class User():
    def __init__(self, obj):
        self.obj = obj

    def login(self):
        if settings.STATUS:
            print('您已登陆')
            return
        dic = {'operator': 'login'}
        self.obj.my_send(dic)
        while True:
            user_name = input('请输入用户名(Q)：').strip()
            if not self.obj.qu_fun(user_name, 'user_name'):return
            user_pwd = input('请输入用户密码：').strip()
            user_info = {'user_name': user_name, 'user_pwd': user_pwd}
            self.obj.my_send(user_info)
            status_dic = self.obj.my_recv()
            if not status_dic['operator']:print('登陆失败，请重新登陆')
            else:
                print('登陆成功')
                settings.STATUS.append(user_name)
                settings.USER_DIR = os.path.join(settings.CLI_DIR, settings.STATUS[0])
                if not os.path.exists(settings.USER_DIR): os.makedirs(settings.USER_DIR)
                break

    def register(self):
        if settings.STATUS:
            print('您已登陆,请先退出在注册新用户')
            return
        dic = {'operator': 'register'}
        self.obj.my_send(dic)
        user_name = input('请输入用户名：').strip()
        while True:
            user_pwd = input('请输入用户密码：').strip()
            user_pwd2 = input('请输入确认密码：').strip()
            if user_pwd == user_pwd2: break
        user_info = {'user_name': user_name, 'user_pwd': user_pwd}
        self.obj.my_send(user_info)
        status_dic = self.obj.my_recv()
        if status_dic['operator']:print('注册成功')
        else: print('用户名已存在，请重新注册')




