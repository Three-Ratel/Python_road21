#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Lock, Thread

lock = Lock()


def eat1(name, lock):
    lock.acquire()
    print('%s抢到面了' % name)
    print('%s抢到叉子了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    print('%s放下叉子了' % name)
    print('%s放下面了' % name)
    lock.release()


def eat2(name, lock):
    lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s抢到面了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    print('%s放下面了' % name)
    print('%s放下叉子了' % name)
    lock.release()


lst = ['henry', 'echo', 'dean', 'daniel']
Thread(target=eat1, args=(lst[0], lock)).start()
Thread(target=eat2, args=(lst[1], lock)).start()
Thread(target=eat1, args=(lst[2], lock)).start()
Thread(target=eat2, args=(lst[3], lock)).start()
