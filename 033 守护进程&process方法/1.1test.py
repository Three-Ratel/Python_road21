#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process


def func():
    while True:
        time.sleep(0.5)
        print(os.getpid(), 'is func')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True
    p.start()
    time.sleep(2)

