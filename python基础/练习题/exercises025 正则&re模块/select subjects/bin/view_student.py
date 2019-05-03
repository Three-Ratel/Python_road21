#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, pickle
from config import settings


def view_student():
    if not os.path.exists(settings.STUDENT_LIST):
        print('学生账号信息为空')
        return
    f = open(settings.STUDENT_LIST, mode='rb')
    while True:
        try:
            v = pickle.load(f)
            if v.name == 'admin' or v.name == 'Admin':
                continue
            print(v.name)
        except:
            break
    f.close()
    input('按enter键结束')

