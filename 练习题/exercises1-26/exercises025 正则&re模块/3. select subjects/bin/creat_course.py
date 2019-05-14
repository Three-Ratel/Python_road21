#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os, pickle
    from config import settings
    from bin import course
    from lib import logger


    def creat_course():
        while True:
            name = input('please input the course name(N/n): ').ljust(8)
            if name.strip().upper() == 'N':
                break
            """
            先判断课程是否存在，存在则不再创建
            """
            if not os.path.exists(settings.COURSE_LIST):
                with open(settings.COURSE_LIST, mode='ab') as f:
                    pass

            f = open(settings.COURSE_LIST, mode='rb')
            flag = False
            while True:
                try:
                    v = pickle.load(f)
                    if v.name == name:
                        flag = True
                        print('课程信息已存在，请重新输入')
                        break
                except:
                    break
            f.close()
            if flag:
                continue
            else:
                price = input('please input the course price: ').ljust(8)
                period = input('please input the course period: ').ljust(8)
                teacher = input('please input the course teacher: ').ljust(8)
                val = course.Course(name, price, period, teacher)
                with open(settings.COURSE_LIST, mode='ab') as f:
                    pickle.dump(val, f)

except Exception as e:
    logger.logger(e)
