#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo:
    def __init__(self):
        self.name = 123


def func(self, a, b):
    print(self.name, a, b)
    # python内部装饰器


@classmethod
def f(cls, a, b):
    print(a, b)


Foo.f(1, 2)
obj.f(1, 2)  # 不推荐


staticmethod
