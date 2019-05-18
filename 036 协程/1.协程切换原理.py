#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time


def func1():
    print(2 + 3)
    yield 1
    time.sleep(1)
    print('end')


def func2():
    g = func1()
    print(next(g))
    next(g)

func2()