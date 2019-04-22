#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = range(10)
# print(type(v))
# val = dir(v)
# for i in val:
#     print(i)


import os

print('============================')


def li_file(dirname):
    for a, b, c in os.walk(dirname):
        for i in c:
            path = os.path.abspath(a)
            v = os.path.join(path, i)

            print(v)


li_file('/Users/henry/programme/python/Python_codes/day014 函数补充&模块os&sys')
