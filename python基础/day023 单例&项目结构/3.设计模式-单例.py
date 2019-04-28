#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
使用__new__方法设计单例
单例(Singleton)模式，无论是实例化多少次，都用第一次创建的那个对象，内存地址一样
"""

# class Singleton(object):
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance
#
#
# obj1 = Singleton()  # 内存地址一致
# obj2 = Singleton()
# print(id(obj1), id(obj2))







