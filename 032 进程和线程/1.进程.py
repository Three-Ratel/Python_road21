#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from multiprocessing import Process


def func():
    print('start', os.getpid())
    time.sleep(1)
    print('end', os.getpid())


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    print('main', os.getpid())




