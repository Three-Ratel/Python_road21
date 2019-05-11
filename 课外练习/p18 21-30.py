#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
21. 如何判断一个值是函数还是方法
"""
# 1. 根据定义参数，方法有一个self形参，函数没有
# 2. 根据调用方式不同，函数调用是fun()，方法一般需要对象调用


"""
22. 请编写一个函数实现ip地址转换为和一个整数
"""


# def ip_transfer(ip):
#     print(int(''.join([bin(int(i)).replace('0b', '').zfill(8) for i in ip.split('.')]), base=2))
#
#
# ip_transfer('192.168.12.87')


"""
23. lambda 表达式以及应用场景
"""
# lambda 表达式又称为匿名函数，主要用于替换简单函数缩减代码量

"""
24. pass作用
"""
# python语法需要，在不需做任何操作的情况下使用

"""
25. *arg 和 **kwargs作用
"""
# 在定义函数时一般使用这两个参数
# *arg可以接收无限个位置参数形成一个元组
# **kwargs可以接收无限个关键字参数形成一个字典

"""
26. 如何在函中设置一个全局变量
"""
# 使用global关键字，先找到改变量，在进行赋值操作


"""
27. 看代码写结果
"""
# # 示例1
# def func(a, b=[]):
#     b.append(a)
#     print(b)
#
#
# func(1)
# func(1)
# func(1)
# func(1)
#
# # [1] [1, 1] [1, 1, 1] [1, 1, 1, 1]
#
# # 示例2
# def func(a, b={}):
#     b[a] = 'v'
#     print(b)
#
#
# func(1)
# func(2)
#
# # {1: 'v'}
# # {1: 'v', 2: 'v'}


"""
28. 看代码写结果：lambda
"""
# def num():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in num()])

# [6, 6, 6, 6]


"""
29. 简述yield和yield from 关键字
"""
# yield：用于定义生成器函数，yield后的值在for循环的时候会生成
# yield from：用于生成器函数中，调用其他函数或生成器函数


"""
30. 有processFunc变量，初始化为processFunc = collapse  and (lambda s:''.join(s.split()))) or (lambda s:s)
"""















