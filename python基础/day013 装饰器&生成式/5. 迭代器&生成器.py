#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = [1, 2, 3, 4]
# val = iter(v)
# value = val.__next__()
# print(value)
# value = val.__next__()
# print(value)
# value = val.__next__()
# print(value)
# value = val.__next__()
# print(value)
# # value = val.__next__()
# # print(value)
#
# print(dir(v))
# print(dir(val))


"""
生成器
"""
def func():
    yield[1, 2, 3, 4]


print(func())
for i in func():
    print(i)

print(dir(func()))

