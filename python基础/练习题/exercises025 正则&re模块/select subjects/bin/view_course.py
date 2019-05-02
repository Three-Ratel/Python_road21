#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle, os, sys

PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PATH)
path = os.path.join(PATH, 'db')
course_list = os.path.join(path, 'course_list.txt')


def view_course():
    if not os.path.exists(course_list) or os.path.getsize(course_list) == 0:
        print('课程信息为空')
        return
    f = open(course_list, mode='rb')
    print('num'.ljust(8), 'titile'.ljust(8), 'price'.ljust(8),  'period'.ljust(8), 'teacher'.ljust(8))
    i = 1
    while True:
        try:
            v = pickle.load(f)
            print(('%s' % i).ljust(8), v.name, v.price, v.period, v.teacher)
            i += 1
        except:
            input('按enter键返回')
            break
    f.close()


if __name__ == '__main__':
    view_course()
