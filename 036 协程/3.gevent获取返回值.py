#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gevent
from gevent import monkey, time

monkey.patch_all()


def func1(i):
    print(123)
    time.sleep(1)
    return i, 'func1'


def func2(i):
    print(456)
    time.sleep(2)
    return i, 'func2'


g1 = gevent.spawn(func1, 1)
g2 = gevent.spawn(func2, 2)
gevent.joinall([g1, g2])
print(g1.value, g2.value)
print('main')
