#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import pickle
    from config import settings
    from lib import logger

    def view_select():
        f = open(settings.SELECT_INFO, mode='rb')
        while True:
            try:
                user_info = pickle.load(f)
                print('用户：', user_info['name'].ljust(6), end=''.ljust(6))
                print('所选课程：', end='')
                for i in user_info['course']:
                    print(i.ljust(6), end='')
                print('')
            except:
                break
        f.close()

except Exception as e:
    logger.logger(e)
