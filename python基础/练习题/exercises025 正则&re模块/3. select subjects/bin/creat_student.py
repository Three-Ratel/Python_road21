#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os, pickle

    from config import settings
    from lib import get_md5, logger
    from src import student


    def creat_student():
        while True:
            name = input('please input the user name(N/n): ')
            if name.upper() == 'N':
                break
            pwd = get_md5.get_md5('123')
            val = student.Student(name, pwd)

            """
            先判断用户是否存在，存在则不再创建
            """
            if not os.path.exists(settings.STUDENT_LIST):
                with open(settings.STUDENT_LIST, mode='ab') as f:
                    pickle.dump(val, f)
                continue

            f = open(settings.STUDENT_LIST, mode='rb')

            flag = False
            while True:
                try:
                    v = pickle.load(f)
                    if v.name == name:
                        flag = True
                        print('学生信息已存在，请重新输入')
                        break
                except:
                    break
            f.close()
            if not flag:
                with open(settings.STUDENT_LIST, mode='ab') as f:
                    pickle.dump(val, f)

except Exception as e:
    logger.logger(e)
