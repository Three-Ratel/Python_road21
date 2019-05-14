#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue

n = 100


def func():
    global n
    n -= 1


li = []
for i in range(10):
    p = Process(target=func)
    p.start()
    li.append(p)

for p in li: p.join()
print(n)
