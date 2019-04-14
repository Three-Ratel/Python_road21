#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
函数属于funcion 类
"""
# def fun ():
#   pass
# print(type(fun))

"""
函数的赋值
"""
# def func():
#   print(123)
# v1 = [func, func, func]
# v2 = [func(), func(), func()]
# print(v1)
# print(v2)


"""
函数传参
"""
# def func(arg):
#   print(arg)
# def show():
#   return 999
# func(show)

"""
输入指定字符，调用指定函数
"""
# 10 个函数
def func():
  print('话费查询')
def bar():
  print('***')
def base():
  print('***')

info = {
    'f1': func,
    'f2': bar,
    'f3': base
  }
choice = input('please input your choice: ')
name = info.get(choice)
if not name:
    print('输入不存在')
else:
    name()

