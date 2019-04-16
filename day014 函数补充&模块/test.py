#!/usr/bin/env python
# -*- coding:utf-8 -*-


def x(a):
    def wrapper(func):
        def inner():
            return [func() for i in range(a)]
        return inner
    return wrapper


@x(9)
def index():
    return 8


v = index()
print(v)



