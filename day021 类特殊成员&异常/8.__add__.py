#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
对象多了怎么办，加起来不就成一个了
"""


class Foo(object):
    def __init__(self):
        self.v = 123

    def __add__(self, other):
        return self.v + other.v


obj1 = Foo()
obj2 = Foo()
v = obj1 + obj2
print(v)


