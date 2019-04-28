#!/usr/bin/env python
# -*- coding:utf-8 -*-


def func():
    def inner():
        pass
    return inner


v = func()
print(v)   # inner 函数


# ##############################
def func(arg):
    def inner():
        print(arg)
    return inner


v1 = func(1)   # 1
v2 = func(2)   # 2


# ##############################
def func(arg):
    def inner():
        arg()
    return inner


def f1():
    print(123)


v = func(f1)
v()		# 123


# ##############################
def func(arg):
    def inner():
        arg()
    return inner


def f1():
    print(123)
    return 666


result = func(f1)()
print(result)
# 执行inner函数 / f1含函数 -> 123 print(result)
# None


# ##############################
def func(arg):
    def inner():
        return arg()
    return inner


def f1():
    print(123)
    return 666


result = func(f1)()
print(result)  # 123 666

