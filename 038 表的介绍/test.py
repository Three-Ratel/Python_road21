#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gevent
from gevent import time


def func1():
    print(123)
    time.sleep(0.1)
    print(456)
    return 'func1'


def func2():
    print('hello')
    time.sleep(0.1)
    print('henry')
    return 'func2'


f1 = gevent.spawn(func1)
f2 = gevent.spawn(func2)
gevent.joinall([f1, f2])
print(f1.value, f2.value)
