#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle, os, sys

PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from lib import get_md5
from config import settings

path = os.path.join(PATH, 'db')
student_list = os.path.join(path, 'student_list.txt')


def login():
    if not os.path.exists(student_list) or os.path.getsize(student_list) == 0:
        return
    f = open(student_list, mode='rb')
    flag = False
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
        except:
            f.close()
            break
    if not flag:
        print('用户名或密码错误,请重新登陆')
        login()


if __name__ == '__main__':
    login()
