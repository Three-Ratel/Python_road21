#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Manager, Lock, Process


def func(dic, lock):
    # with lock:
        dic['count'] -= 1


if __name__ == '__main__':
    # m = Manager()
    lock = Lock()
    with Manager() as m:
        lock = Lock()
        dic = m.dict({'count': 100})  # 共享的dict
        p_l = []
        for i in range(100):
            p = Process(target=func, args=(dic, lock))
            p.start()
            p_l.append(p)
        for p in p_l: p.join()
        print(dic)
