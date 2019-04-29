#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os
    import sys
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_PATH)
    from config import settings
    from lib import encrypt
    from lib import logger



    def register():
        """
        用户注册
        :return:
        """
        print('用户注册')
        while True:
            user = input('请输入用户名(N返回上一级)：')
            if user.upper() == 'N':
                return
            pwd = input('请输入密码：')
            if user in settings.USER_DICT:
                print('用户已经存在，请重新输入。')
                continue
            settings.USER_DICT[user] = encrypt.encrypt_md5(pwd)
            print('%s 注册成功' % user)
            print(settings.USER_DICT)


    def login():
        """
        用户登录
        :return:
        """
        print('用户登录')
        while True:
            user = input('请输入用户名(N返回上一级)：')
            if user.upper() == 'N':
                return
            pwd = input('请输入密码：')
            if user not in settings.USER_DICT:
                print('用户名不存在')
                continue

            encrypt_password = settings.USER_DICT.get(user)
            if encrypt.encrypt_md5(pwd) != encrypt_password:
                print('密码错误')
                continue

            print('登录成功')
            settings.CURRENT_USER = user
            return
except Exception as e:
    logger.logger(e)


if __name__ == '__main__':
    register()
    login()



