#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process, JoinableQueue


def producer(q, user, food):
    for i in range(10):
        q.put('%s生产了%s' % (user, food))
    q.join()


def consumer(q, user, food):
    while True:
        q.get()
        print('%s吃了%s' % (user, food,))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p_l = []
    for i in range(2):
        p = Process(target=producer, args=(q, 'henry%s' % (i + 1,), 'food'))
        p.start()
        p_l.append(p)
    c = Process(target=consumer, args=(q, 'echo', 'food'))
    c.daemon = True
    c.start()
    for i in p_l: i.join()
    # c.terminate()


from threading import enumerate