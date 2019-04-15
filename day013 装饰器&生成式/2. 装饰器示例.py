#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
"""
示例一
"""


# def func(arg):
#     def inner():
#         print('before')
#         v = arg()
#         print('after')
#         return v
#     return inner
#
#
# def index():
#     print('123')
#     return 666
#
#
# # 示例
# print('-------1--------')
# index()
#
# print('-------2--------')
# func(index)()
#
# print('-------3--------')
# index = func(index)
# index()
#
# print('-------4--------')
# index = func(index)
# index()

"""
示例二
"""


def func(arg):
    def inner():
        return arg()
    return inner


@func
def index():
    print(123)
    return 666


print(index)



"""
示例三：计算函数执行时间
"""


# def wrapper(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(end_time - start_time)
#         return func()
#     return inner
#
#
# @wrapper
# def f1():
#     time.sleep(2)
#     print(123)
#
#
# f1()
#
#
# @wrapper
# def f2():
#     time.sleep(1.5)
#     print(123)
#
#
# f2()
# 判断用户是否登陆


