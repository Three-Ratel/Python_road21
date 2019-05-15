#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread
n = 100


def son():
    global n
    n -= 1


t_l = []
for i in range(100):
    t = Thread(target=son)
    t_l.append(t)
    t.start()

for t in t_l: t.join()
print(n)
