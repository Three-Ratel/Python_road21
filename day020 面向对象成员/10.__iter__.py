#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 __iter__
"""


class Foo(object):

    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)


obj = Foo([11, 22, 33, 44])

for i in obj:
    print(i)


obj = iter([11, 22, 33, 44])

while True:
    val = obj.next()
    print(val)

