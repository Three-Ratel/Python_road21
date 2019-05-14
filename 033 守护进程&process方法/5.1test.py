#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import queue
from multiprocessing import Process, Queue


def func(exp, q):
    v = eval(exp)
    q.put(v)


if __name__ == '__main__':
    q = Queue()
    p = Process(target=func, args=('1*2*3', q))
    p.start()
    print('main', os.getpid(), 'res = %s' % q.get())
    try:
        q.get_nowait()
    except queue.Empty:
        print('here')
