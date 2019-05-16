#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread, Lock

a = 0


def add_f(lock):
    global a
    with lock:
        for i in range(2000000):
            a += 1


def sub_f(lock):
    global a
    with lock:
        for i in range(2000000):
            a -= 1


lock = Lock()
t1 = Thread(target=add_f, args=(lock,))
t1.start()
t2 = Thread(target=sub_f, args=(lock,))
t2.start()
t1.join()
t2.join()
print(a)






# import dis
# print(dis.dis(func2))


"""
示例2
"""
# from threading import Thread, Lock
# import os, time
#
#
# def work(lock):
#     with lock:
#         global n
#         temp = n
#         time.sleep(0.01)
#         n = temp - 1
#
#
#
# n = 100
# l = []
# lock = Lock()
# for i in range(100):
#     p = Thread(target=work, args=(lock,))
#     l.append(p)
#     p.start()
# for p in l:
#     p.join()
#
# print(n)
