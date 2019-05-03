#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, pickle
from config import settings


def select_course():
    info = {}
    info['course'] = set()
    while True:
        course_num = input('请输入要选择课程序号(N/n)：').strip()
        if course_num.upper() == 'N':
            return

        f = open(settings.COURSE_LIST, mode='rb')
        i = 1
        flag1 = False
        while True:
            try:
                v = pickle.load(f)
                print(('%s' % i).ljust(8), v.name, v.price, v.period, v.teacher)
                if str(i) == course_num:
                    flag1 = True
                    info['name'] = settings.USER
                    if v.name not in info['course']:
                        info['course'].add(v.name)

                i += 1
            except:
                break
        if not flag1:
            print('输入有误，请重新输入')
            continue
        f.close()

        """
        把选课信息写入文件
        """
        f1 = open(settings.SELECT_INFO1, mode='ab')
        f = open(settings.SELECT_INFO, mode='rb')
        flag = False
        while True:
            try:
                user_info = pickle.load(f)
                if info['name'] == user_info['name']:
                    flag = True
                    user_info['course'] = user_info['course'].union(info['course'])
                    print('已选课程', user_info['course'])
                pickle.dump(user_info, f1)
            except:
                break
        f.close()
        f1.close()
        if not flag:
            print('已选课程', info['course'])
            f1 = open(settings.SELECT_INFO1, mode='ab')
            pickle.dump(info, f1)
            f1.close()
        os.remove(settings.SELECT_INFO)
        os.rename(settings.SELECT_INFO1, settings.SELECT_INFO)




