#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo:
    def __init__(self):
        self.name = 123

    def func(self, a, b):
        print(self.name, a, b)

    # python内部装饰器
    @staticmethod
    def f():
        print(1, 2)


Foo.f()
obj = Foo()
obj.func(1, 2)
obj.f()




