#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1. 类成员
"""
# class Foo(object):
#
#     @staticmethod
#     def func():
#         print('给你说，可以吧')
#
#     @classmethod
#     def f(cls):
#         print('给你说，这也可以吧')
#
#     @property
#     def fun(self):
#         print('括号也省了')
#
#
# Foo.func()
# Foo.f()
# Foo().fun


"""
2. 特殊方法
"""
# class Foo(object):
#     def __new__(cls, *args, **kwargs):  # 在 __init__ 之前
#         return 'henry'
#         # object.__new__(cls)
#
#
# obj = Foo()
# print(obj)
# obj.age = '18'      # 会报错
# print(obj)

# class Foo:
#     def __str__(self):
#         print('变样是不是不认识我了')
#         return 'henry'
#
#
# obj = Foo()
# print(obj)


"""
反射
"""

# # getattr示例
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#
# obj = Foo('alex')
# v1 = getattr(obj, 'name')
# print(v1)
#
# # setattr示例
# print(obj.name)
# setattr(obj, 'name', 'eric')
# print(obj.name)

"""
modules
"""
# v = [1,2,3,4]
# import random
# random.shuffle(v)
# print(v)

"""
sys.modules
"""
# import sys
# print(type(sys.modules))

"""
time
"""
# import time
# # print(time.timezone)
#
# from datetime import timezone, timedelta, datetime
# tz = timezone(timedelta(hours=7))
# print(tz)
# tz_7 = datetime.now(tz)
# print(tz_7)
#
# v = datetime.now().timestamp()
# print(v)
# print(time.time())
#
#
# v = datetime.now().strftime('%Y-%m-%d')
# print(v)
#
# v = datetime.strptime('2019-04-19', '%Y-%m-%d')
# print(v)
#
# v = datetime.fromtimestamp(time.time(), tz)
# print(v)


"""
importlib
"""
# import importlib
# importlib.import_module('os')
# os = __import__('os')
# print(os.path.abspath('__name__'))

"""
collections
"""
from collections import OrderedDict

a = OrderedDict()
print(a, type(a))




