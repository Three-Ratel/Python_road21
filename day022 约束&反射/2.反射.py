#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo(object):
    def __init__(self, name):
        self.name = name


obj = Foo('alex')
print(obj.name)

v1 = getattr(obj, 'name')
print(v1)

setattr(obj, 'name', 'eric')
print(obj.name)





