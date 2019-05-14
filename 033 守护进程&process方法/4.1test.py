#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process

n = 100


def func():
    global n
    n -= 1


if __name__ == '__main__':
    p = Process()
    p.start()
    print(n)
