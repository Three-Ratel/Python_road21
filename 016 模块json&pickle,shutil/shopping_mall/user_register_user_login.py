# !/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime


def user_register():
    """
    用户注册功能
    content：要写入文件的内容
    users_list.txt：存放用户列表的文件
    :return: None
    """
    while True:
        li = []
        user_name = input('please enter user name(N/n exit): ')
        if user_name.upper() == 'N':
            return
        while True:
            user_pwd = input('please enter your password: ')
            user_pwd2 = input('please ensure your password: ')
            if user_pwd != user_pwd2:
                continue
            rtime = datetime.now()
            rtime = rtime.strftime('%Y/%m/%d %H:%M:%S')
            break
        li = [user_name, user_pwd, rtime]
        content = ','.join(li)
        f = open('users_list.txt', mode='a+', encoding='utf-8')
        f.write(content + '\n')
        f.close()


def user_login():
    """
    flag：标记用户登陆是否成功
    info：存放用户登陆次数，如果次数为3则直接退出，并提示用户已经冻结
    :return:
    """
    flag = '用户名或密码错误'
    info = {}
    while True:
        log_name = input('please enter user name(N/n exit): ')
        if log_name.upper() == 'N':
            return
        """
        如果用户在BLACK_LIST中，直接退出
        """
        if log_name in BLACK_LIST:
            print('该用户已冻结')
            return

        log_pwd = input('please enter your pwd: ')
        f = open('users_list.txt', mode='r', encoding='utf-8')
        for i in f:
            if not i.strip():
                print('用户列表为空')
            u, v, w = i.strip().split(',')
            if u == log_name and v == log_pwd:
                flag = '登陆成功'
                print(flag)
                return
        print(flag)
        if info.get(log_name):
            info[log_name] = info[log_name] + 1
        else:
            info[log_name] = 1
        print(info)
        for u, v in info.items():
            if v == 3:
                BLACK_LIST.append(u)
                print('用户已冻结')
                break

BLACK_LIST = []





