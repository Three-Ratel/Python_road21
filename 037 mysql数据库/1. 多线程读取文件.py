#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.有一个文件，这个文件中有20000行数据，开启一个线程池，为每100行创建一个任务，打印这100行数据。
"""


# from copy import copy
# from concurrent.futures import ThreadPoolExecutor
#
#
# def print_line(lines):
#     print(lines)
#
#
# tp = ThreadPoolExecutor(20)
# with open('userinfo', mode='r', encoding='utf-8') as f:
#     lines = []
#     for i in f:
#         lines.append(i.strip())
#         if len(lines) == 100:
#             tp.submit(print_line, copy(lines))
#             lines.clear()
#     if lines: tp.submit(print_line, copy(lines))


def print_line(lines):
    print(lines)


def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            yield line


def submit_func(tp, line=None, end=False, lines=[]):
    if line: lines.append(line.strip())
    if len(lines) == 100 or end:
        tp.submit(print_line, copy(lines))
        lines.clear()


from copy import copy
from concurrent.futures import ThreadPoolExecutor

tp = ThreadPoolExecutor(20)
for line in read_file('userinfo'):
    submit_func(tp, line)
submit_func(tp, end=True)

"""
单线程
"""
# from threading import Lock
# from concurrent.futures import ThreadPoolExecutor
#
#
# def read(f, lock):
#     lock.acquire()
#     data = f.readline().strip()
#     if not data:return
#     print(data)
#     lock.release()
#
#
# lock = Lock()
# tp = ThreadPoolExecutor(20)
# with open('userinfo', mode='r', encoding='utf-8') as f:
#     for i in range(1, 20001):
#         t = tp.submit(read, f, lock)
#     tp.shutdown()


# with open('userinfo', mode='w', encoding='utf-8') as f:
#     for i in range(1,20001):
#         f.write(str(i) + '\n')
