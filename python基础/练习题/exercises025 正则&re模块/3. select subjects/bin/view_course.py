#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import pickle, os
    from config import settings
    from lib import logger


    def view_course():
        if not os.path.exists(settings.COURSE_LIST) or os.path.getsize(settings.COURSE_LIST) == 0:
            print('课程信息为空')
            return
        f = open(settings.COURSE_LIST, mode='rb')
        print('num'.ljust(8), 'titile'.ljust(8), 'price'.ljust(8),  'period'.ljust(8), 'teacher'.ljust(8))
        i = 1
        while True:
            try:
                v = pickle.load(f)
                print(('%s' % i).ljust(8), v.name, v.price, v.period, v.teacher)
                i += 1
            except:
                break
        f.close()
        input('按enter键结束')


    if __name__ == '__main__':
        view_course()

except Exception as e:
    logger.logger(e)
