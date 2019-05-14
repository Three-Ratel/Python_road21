#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime


def log(func):
    def inner(*args, **kwargs):
        func()
        asctime = datetime.datetime.now()
        c_time = asctime.strftime('%Y-%m-%d %H:%M:%S')
        print(c_time, '%s被调用了' % (func.__name__,))

    return inner


@log
def func():
    print('blablabla')


func()
