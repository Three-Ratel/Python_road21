#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import time
import gevent
from gevent import monkey, time
monkey.patch_all()


def func1():
    print(123)
    time.sleep(3)
    print(456)


def func2():
    print('---------')
    time.sleep(1)
    print('=========')


g1 = gevent.spawn(func1)
g2 = gevent.spawn(func2)
gevent.joinall([g1, g2])
print('main')
