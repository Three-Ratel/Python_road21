#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = [i if i > 5 else i+1 for i in range(5) if i > 0]
# print(v)

"""
新浪面试题
"""
def num():
    return [lambda x: x * i for i in range(4)]


li = [m(2) for m in num()]

print(li)

