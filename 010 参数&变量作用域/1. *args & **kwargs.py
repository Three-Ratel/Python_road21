#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
*args
"""
# def func(*args):
# 	print(args)
#
# # [1, 2, 3]会被当成整体变成tuple中的一个元素
# func(1, 2, 3, [1, 2, 3])
#
# # 直接赋值, [1, 2, 3]也会循环取出追加到tuple中
# func(4, 5, 6, *[1, 2, 3])

"""
**kwargs
"""
# def func(**kwargs):
#     print(kwargs)
#
# # [1, 2, 3]会被当成整体变成dict中 'd': [1, 2, 3]
# func(a=1, b=2, c=3, d=[1, 2 ,3])
# # 直接赋值, {'k1': 4, 'k2': 5}也会循环取出追加到形参的dict中
# func(a=1, b=2, c=3, d=[1, 2, 3], **{'k1': 4, 'k2': 5})

