#!/usr/bin/env python
# -*- coding:utf-8 -*-


# def func():
#     return 111111
#     yield 1
#
# v = func()
# print(v)


"""
示例：读取文件
"""


def func():
    curse = 0
    while True:
        f = open('db', mode='r', encoding='utf-8')
        f.seek(curse)
        data_list = []
        for i in range(10):
            line = f.readline()
            if not line:
                return
        data_list.append(line)
        curse = f.tell()
        f.close
        for row in data_list:
            yield row

v = func()
for i in v:
  print(i)
