#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
列表生成式
"""


def num():
    print(123)
    return [lambda x: x * i for i in range(4)]


print([m(2) for m in num()])



