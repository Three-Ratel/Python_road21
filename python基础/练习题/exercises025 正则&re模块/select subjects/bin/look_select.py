#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
from config import settings


def look_select():
    flag = False
    f = open(settings.SELECT_INFO, mode='rb')
    while True:
        try:
            user_info = pickle.load(f)
            if settings.USER != user_info['name']:
                continue
            flag = True
            print('用户：', settings.USER)
            print('所选课程：', end='')
            for i in user_info['course']:
                print(i.ljust(6), end='')
            print('')
            break
        except:
            break
    f.close()
    if not flag:
        print('还没有选择任何课程')

    input('按enter键结束')


