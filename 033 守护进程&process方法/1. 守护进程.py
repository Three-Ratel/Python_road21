#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from multiprocessing import Process


def son1():
    while True:
        print(123)
        time.sleep(0.5)


def son2():
    for i in range(5):
        print(123)
        time.sleep(0.5)


if __name__ == '__main__':
    p = Process(target=son1)
    p.daemon = True
    p.start()
    time.sleep(2)





