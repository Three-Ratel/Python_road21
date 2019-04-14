#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
w+ 先写在读，否则没有意义, 也就是写读
"""

# with open('b.txt', mode='w+', encoding='utf-8') as v:
#
#     v2 = v.write('123')
#     v.seek(0)
#     v1 = v.read()
#
# print(v2)
# print(v1)



""" 
r+  先读，在写
"""
# with open('b.txt', mode='r+', encoding='utf-8') as v:
#
#     v2 = v.write('你好')
#     v.seek(0)
#     v1 = v.read()
#
#
# print(v2)
# print(v1)


"""
a+ 先追加在读
"""

# with open('b.txt', mode='a+', encoding='utf-8') as v:
#
#     v2 = v.write('123')
#     v.seek(0)
#     v1 = v.read()
#
# print(v2)
# print(v1)

