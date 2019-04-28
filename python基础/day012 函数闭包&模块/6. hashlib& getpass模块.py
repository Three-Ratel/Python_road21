#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib

"""
md5加密
"""
def get_data_md5(data):
    obj = hashlib.md5()
    obj.update(str(data).strip('[]{}()').encode('utf-8'))
    v = obj.hexdigest()
    return v

"""
用户注册
"""
def user_register():

    while True:
        user_name = input('请输入注册用户名(Q/q退出): ')
        if user_name.upper() == 'Q':
            break
        f = open('user_list.txt', mode='r', encoding='utf-8')
        f1 = str(f.readlines(1)).strip()
        if f1:
            a = True
            for i in f:
                u, v = i.split(':')
                if user_name == u:
                    a = False
                    print('用户名已存在')
                    break
            if a:
                pass
            else:
                continue

        user_pwd = input('请输入密码: ')
        user_pwd2 = input('请确认密码: ')
        if user_pwd != user_pwd2:
            print('两次密码不一致')
            continue
        user_pwd = get_data_md5(user_pwd)

        # 把用户账号和密码写入文件
        f = open('user_list.txt', mode='a', encoding='utf-8')
        msg = user_name + ':' + user_pwd + '\n'
        f.write(msg)
        f.flush()
    f = open('user_list.txt', mode='a', encoding='utf-8')
    f.close()


"""
用户登陆
"""
def user_log_on():
    name = input('请输入用户名: ')
    pwd = get_data_md5(input('请输入用户密码: '))
    with open('user_list.txt', mode='r', encoding='utf-8') as f:
        for i in f:
            u, v = i.strip().split(':')
            if name == u and pwd == v:
                print('登陆成功')
                return True

    print('登陆失败')

user_register()
user_log_on()


