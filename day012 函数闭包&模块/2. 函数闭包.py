#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
练习1  （函数嵌套关系和变量使用）
"""
# name = 'henry'
# def func():
#     print(name)
# def bar():
#     name = 'echo'
#     print(name)
#     func()
#
# bar()

"""
练习2
"""
# info = []
# def func():
#     print(items)
#
# for items in range(10):
#     info.append(func)
#
# info[0]()

"""
练习3  （闭包应用） 重点
"""
info = []
def func(i):
    def inner():
        print(i)
    return inner

for items in range(10):
    info.append(func(items))

info[0]()
info[1]()
info[4]()

