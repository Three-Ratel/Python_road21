#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import random
from multiprocessing import Process, Queue


def producer(q, name, food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s' % (food, i)
        q.put(fd)
        print('%s生产了一个%s' % (name, food))


def consumer(q, name):
    while True:
        food = q.get()
        if not food:
            q.put(None)
            break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (name, food))


def cp(num1, num2):
    q = Queue(10)
    p_l = []
    for i in range(num1):
        p = Process(target=producer, args=(q, 'henry', 'food'))
        p.start()
        p_l.append(p)
    for i in range(num2):
        c = Process(target=consumer, args=(q, 'echo%s' % (i+1,)))
        c.start()
    for i in p_l:i.join()
    q.put(None)


if __name__ == '__main__':
    cp(1, 4)





