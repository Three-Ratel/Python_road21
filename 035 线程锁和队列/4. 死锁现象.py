#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Thread, Lock

noodle_lock = Lock()
fork_lock = Lock()


def eat1(name, noodle_lock, fork_lock):
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    fork_lock.release()
    print('%s放下叉子了' % name)
    noodle_lock.release()
    print('%s放下面了' % name)


def eat2(name, noodle_lock, fork_lock):
    fork_lock.acquire()
    print('%s抢到叉子了' % name)
    noodle_lock.acquire()
    print('%s抢到面了' % name)
    print('%s吃了一口面' % name)
    time.sleep(0.1)
    noodle_lock.release()
    print('%s放下面了' % name)
    fork_lock.release()
    print('%s放下叉子了' % name)


lst = ['henry', 'echo', 'dean', 'daniel']
Thread(target=eat1, args=(lst[0], noodle_lock, fork_lock)).start()
Thread(target=eat2, args=(lst[1], noodle_lock, fork_lock)).start()
Thread(target=eat1, args=(lst[2], noodle_lock, fork_lock)).start()
Thread(target=eat2, args=(lst[3], noodle_lock, fork_lock)).start()

# 锁
# 互斥锁
# 在一个线程中连续多次acquire会死锁
# 递归锁
# 在一个线程中连续多次acquire不会死锁
# 死锁现象
# 死锁现象是怎么发生的？
# 1.有多把锁，一把以上
# 2.多把锁交替使用
# 怎么解决
# 递归锁 —— 将多把互斥锁变成了一把递归锁
# 快速解决问题
# 效率差
# ***递归锁也会发生死锁现象，多把锁交替使用的时候
# 优化代码逻辑
# 可以使用互斥锁 解决问题
# 效率相对好
# 解决问题的效率相对低
