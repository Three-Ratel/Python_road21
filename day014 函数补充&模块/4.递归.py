#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
斐波那契数列
"""


def x(num):
    def wrapper(function):
        def inner(*args):
            function(*args)
            return
        return inner
    return wrapper


@x(100)
def func(a, b):
    if b < 100:
        print(b)
    else:
        return
    func(b, a+b)


func(0, 1)


"""
示例
"""
# def func(a):
#     if a == 5:
#         return 100
#     result = func(a+1) + 10
#     print(result)
#     return result
#
#
# v = func(1)

