#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, random
from threading import Thread, RLock


def eat1(name, noddle_lock, fork_lock):
    noddle_lock.acquire()
    print('%s抢到了面条' % name)
    fork_lock.acquire()
    print('%s抢到了叉子' % name)
    print('%s吃了一口面' % name)
    time.sleep(random.random())
    noddle_lock.release()
    fork_lock.release()


def eat2(name, noddle_lock, fork_lock):
    fork_lock.acquire()
    print('%s抢到了叉子' % name)
    noddle_lock.acquire()
    print('%s抢到了面条' % name)
    print('%s吃了一口面' % name)
    noddle_lock.release()
    fork_lock.release()


u_li = ['henry', 'echo', 'dean', 'daniel', 'diane']
fork_lock = noddle_lock = RLock()


Thread(target=eat1, args=(u_li[0], noddle_lock, fork_lock)).start()
Thread(target=eat2, args=(u_li[1], noddle_lock, fork_lock)).start()
Thread(target=eat1, args=(u_li[2], noddle_lock, fork_lock)).start()
Thread(target=eat2, args=(u_li[3], noddle_lock, fork_lock)).start()
Thread(target=eat1, args=(u_li[4], noddle_lock, fork_lock)).start()