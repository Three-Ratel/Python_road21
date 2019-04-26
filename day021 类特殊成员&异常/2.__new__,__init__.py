#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
先执行__new__ 在执行类中的 __init__ 方法
"""


# class Foo(object):
#
#     def __init__(self):
#         self.name = 'henry'
#         self.age = 18
#
#     def __new__(cls, *args, **kwargs):
#         print('哈哈，没想到吧')
#         return object.__new__(cls)
#
#
# obj = Foo()
# print(obj.name, obj.age)


"""
在使用__new__方法时，构造的对象值为  new 方法的返回值
"""
class Foo(object):

    def __new__(cls, *args, **kwargs):
        print('哈哈，没想到吧')
        return 123


obj = Foo()
print(obj)