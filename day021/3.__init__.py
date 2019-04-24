#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
构造方法：自动执行类中的 __init__ 方法
"""


class Foo:

    def __init__(self, name):
        self.name = name
        self.age = 18


obj = Foo('henry')
print(obj.name, obj.age)

