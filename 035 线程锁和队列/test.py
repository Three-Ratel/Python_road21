#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func():
    def producer(i):
        return {'i': i}

    def consumer(dic):
        print(dic.result()['i'])

    li = [i for i in range(0, 20)]
    tp = ThreadPoolExecutor(10)
    for i in li:
        ret = tp.submit(producer, i)
        ret.add_done_callback(consumer)


pp = ProcessPoolExecutor(3)
for i in range(5):
    pp.submit(func)
