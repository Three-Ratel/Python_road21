#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.有一个文件，这个文件中有20000行数据，开启一个线程池，为每100行创建一个任务，打印这100行数据。
"""
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


def read(f, lock):
    lock.acquire()
    data = f.readline().strip()
    print(data)
    lock.release()


lock = Lock()
tp = ThreadPoolExecutor(20)
with open('userinfo', mode='r', encoding='utf-8') as f:
    for i in range(1, 20001):
        t = tp.submit(read, f, lock)
    tp.shutdown()





# with open('userinfo', mode='w', encoding='utf-8') as f:
#     for i in range(1,20000):
#         f.write(str(i) + '\n')
