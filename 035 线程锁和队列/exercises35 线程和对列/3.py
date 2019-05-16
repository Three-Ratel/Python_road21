#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
6.使用线程池，随意访问n个网址，并把网页内容记录在文件中
"""
import requests
import pickle
from concurrent.futures import ThreadPoolExecutor

url = []


def producer(url):
    response = requests.get(url)
    return {'url': url, 'response': response.text}


def consumer(dic):
    with open('net_pages', mode='a', encoding='utf-8') as f:
        f.write(str(dic.result()))
        f.write('\n')


url_l = ['https://www.baidu.com', 'https://www.meijutt.com/alltop_hit.html', 'https://www.cnblogs.com/henryw/',
         'https://www.cnblogs.com']

tp = ThreadPoolExecutor(2)
for url in url_l:
    dic = tp.submit(producer, url)
    dic.add_done_callback(consumer)



"""
7.请简述什么是死锁现象？如何产生？如何解决
"""
# 在一个线程、进程中有多把锁
# 多把锁交替使用
# 使用递归锁、只使用一把锁

"""
8.请说说你知道的并发编程中的哪些锁？各有什么特点？
"""
# 互斥锁：同一进程或线程中只能有一个线程或进程acquire
# 递归锁：递归锁在同一线程中，可以连续acquire多次不会阻塞

"""
9.cpython解释器下的线程是否数据安全？
"""
# cpython中线程数据不安全，线程共享进程中的数据

"""
10.尝试：在多进程中开启多线程。在进程池中开启线程池
"""
"""
在多进程中开启多线程
"""
# from threading import Thread
# from multiprocessing import Process, Queue
#
#
# def func(q):
#     def producer(q, i):
#         q.put(i)
#         print(i)
#
#     def consumer(q):
#         while True:
#             if not q.get():
#                 q.put(None)
#                 break
#             print(q.get())
#
#     # 10个生产者，线程
#     for i in range(1, 11):
#         Thread(target=producer, args=(q, i,)).start()
#
#     # 5个消费者，线程
#     for i in range(2):
#         Thread(target=consumer, args=(q,)).start()
#
#
# q = Queue()
# # 5个进程
# p_l = []
# for i in range(5):
#     p = Process(target=func, args=(q,))
#     p.start()
#     p_l.append(p)
#
# for p in p_l: p.join()
# q.put(None)

"""
进程池中开启线程池
"""
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
#
# def func():
#     def producer(i):
#         return {'i': i}
#
#     def consumer(dic):
#         print(dic.result()['i'])
#
#     li = [i for i in range(0, 20)]
#     tp = ThreadPoolExecutor(10)
#     for i in li:
#         ret = tp.submit(producer, i)
#         ret.add_done_callback(consumer)
#
#
# pp = ProcessPoolExecutor(3)
# for i in range(5):
#     pp.submit(func)
