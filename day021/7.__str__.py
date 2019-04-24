#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
"""


class Foo:

    def __str__(self):
        return 'henry'


obj = Foo()
print(obj)




