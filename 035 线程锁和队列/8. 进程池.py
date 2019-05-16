#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, time, random
from concurrent.futures import ProcessPoolExecutor


def func(i):
    time.sleep(random.random())
    return {'i': i, 'pid': os.getpid()}


def dispose(dic):
    print(dic.result()['i'])


ret_l = []
pp = ProcessPoolExecutor(5)
for i in range(100):
    ret = pp.submit(func, i)
    # ret_l.append(ret)
    ret.add_done_callback(dispose)

# for ret in ret_l:
#     print(ret.result()['i'])
"""
map方式
"""
# ret = pp.map(func, range(100))
# print(ret)
# for ret in ret:
#     print(ret['i'])
