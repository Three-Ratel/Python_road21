#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os, pickle
    from config import settings
    from lib import logger


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

except Exception as e:
    logger.logger(e)
