#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
"""
server： 端的配置信息，及全局变量
USER：登陆成功的用户名
PRO_DIR：项目的绝对路径
DB_PATH：数据信息的目录
SER_DIR：每个用户上传、下载的目录
USER_INFO：存储用户注册信息的文件路径
"""
USER = {}
IP_PORT = ('127.0.0.1', 9000)
PRO_DIE = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(PRO_DIE, 'db')
SER_DIR = os.path.join(DB_PATH, 'server_dir')
USER_INFO = os.path.join(DB_PATH, 'user_info')
USER_DIR = None
"""普通用户配额2G"""
DIR_SIZE = 1024*1024*1024 * 2
"""vip用户配额4G"""
VIP_SIZE = 1024*1024*1024 * 6

"""
client 端的配置信息，及全局变量
PRO_DIR：项目的绝对路径
DB_PATH：数据信息的目录
CLI_DIR：用户的文件的上级目录
STATUS：用户登陆成功后的状态，即用户名
USER_DIR：用户登陆成功后的家目录
"""
PRO_DIE = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(PRO_DIE, 'db')
CLI_DIR = os.path.join(PRO_DIE, os.path.join(DB_PATH, 'client_dir'))
STATUS = []
USER_DIR = None




