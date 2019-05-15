#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Thread
from multiprocessing import Process


def func(a, b):
    a + b


if __name__ == '__main__':
    p_l = []
    start = time.time()
    for i in range(10000):
        p = Process(target=func, args=(i, i * 2))
        p.start()
        p_l.append(p)
    for p in p_l: p.join()
    print(time.time() - start)

    t_l = []
    start = time.time()
    for i in range(10000):
        t = Thread(target=func, args=(i, i * 2))
        t.start()
        t_l.append(t)
    for t in t_l: t.join()
    print(time.time() - start)
