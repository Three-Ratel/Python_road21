#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from greenlet import greenlet


def eat():
    print('henry is eating')
    time.sleep(0.5)
    g2.switch()
    print('henry finished eating')


def sleep():
    print('echo is sleeping')
    time.sleep(0.5)
    print('echo finished sleeping')
    g1.switch()


g1 = greenlet(eat)
g2 = greenlet(sleep)
g1.switch()
