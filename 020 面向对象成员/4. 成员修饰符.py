#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo:
    def __init__(self, name):
        self.__name = name

    def func(self):
        print(self.__name)


obj = Foo('henry')
print(obj._Foo__name)   # 会报错
obj.func()          # 可以访问


# class Foo:
#     __x = 1
#
#     @staticmethod
#     def func():
#         print(Foo.__x)
#
#
# obj = Foo()
# # print(Foo.__x)      # 会报错
# print(obj._Foo__x)  # 强制访问私有成员
