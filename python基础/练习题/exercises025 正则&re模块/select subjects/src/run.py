#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys
PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
from bin import login
from src import admin, student
from config import settings


def run():
    if not settings.USER:
        v = login.login()
        if not v:
            print('没有用户信息')
            exit()

    if settings.USER == 'admin' or settings.USER == 'Admin':
        admin.Admini()()
    else:
        student.Student()()


if __name__ == '__main__':
    run()








