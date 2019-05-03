#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import pickle, os
    from lib import get_md5, logger
    from config import settings


    def login():
        flag = False
        if not os.path.exists(settings.STUDENT_LIST) or os.path.getsize(settings.STUDENT_LIST) == 0:
            return flag

        f = open(settings.STUDENT_LIST, mode='rb')
        name = input('请输入账号：').strip()
        if name.upper() == 'N':
            return
        pwd = input('请输入密码：').strip()
        pwd = get_md5.get_md5(pwd)
        while True:
            try:
                v = pickle.load(f)
                if v.name == name and v.pwd == pwd:
                    print('登陆成功')
                    settings.USER = name
                    settings.PWD = pwd
                    flag = True
                    return flag
            except:
                f.close()
                break
        if not flag:
            print('用户名或密码错误,请重新登陆')
            login()


    if __name__ == '__main__':
        login()

except Exception as e:
    logger.logger(e)

