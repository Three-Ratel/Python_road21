#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. 获取3个百度网页源码，并写入local.html
"""
# import gevent
# import requests
# from gevent import queue
#
#
# def get_page(url, q):
#     response = requests.get(url)
#     response = {'url': url, 'response': response.text}
#     q.put(response)
#     print(url)
#
#
# def write(q):
#     while True:
#         response = q.get()
#         if not response: q.put(None)
#         with open('local.html', mode='a', encoding='utf-8') as f:
#             f.write(response['response'])
#
#
# q = queue.Queue()
# url_l = ['https://www.baidu.com', 'https://www.baidu.com', 'https://www.baidu.com']
# g_l = []
# for url in url_l:
#     g = gevent.spawn(get_page, url, q)
#     g_l.append(g)
#
# for i in range(3):
#     gevent.spawn(write, q)
#
# for g in g_l: g.join()
# q.put(None)


"""
2. 多线程实现消费者、生产者模型
"""
# from queue import Queue
# from threading import Thread
#
#
# def producer(i, q):
#     q.put(i)
#     print('这是生产者%s' % i)
#
#
# def consumer(i, q):
#     print('这是消费者%s' % i)
#     while True:
#         msg = q.get()
#         if not msg:
#             q.put(None)
#             return
#
#
# q = Queue()
# t_l = []
# for i in range(5):
#     t = Thread(target=producer, args=(i, q))
#     t.start()
#     t_l.append(t)
# for i in range(3):
#     Thread(target=consumer, args=(i, q)).start()
# for t in t_l: t.join()
# q.put(None)

"""
3. 开启⼀一个有20个线程的线程池，提交200个任务
"""
# from concurrent.futures import ThreadPoolExecutor
#
#
# def func(i):
#     return i
#
#
# with open('log', mode='a', encoding='utf-8') as f:
#     f.write('start'+'\n')
# th = ThreadPoolExecutor(20)
# res = []
# for i in range(200):
#     ret = th.submit(func, i)
#     res.append(ret.result())
#
# th.shutdown()
# with open('log', mode='a', encoding='utf-8') as f:
#     f.write('end'+'\n')


"""
4. 写程序说明死锁现象是如何产生的，并用文字说明原因，列举解决方案。
"""
# import time
# from threading import Thread, Lock
#
#
# def func1(lock1, lock2):
#     lock1.acquire()
#     print('获得lock1')
#     time.sleep(1)
#     lock2.acquire()
#     print('获得lock2')
#     lock1.release()
#     lock2.release()
#
#
# def func2(lock1, lock2):
#     lock2.acquire()
#     print('获得lock2')
#     time.sleep(1)
#     lock1.acquire()
#     print('获得lock1')
#     lock1.release()
#     lock2.release()
#
#
# lock1 = Lock()
# lock2 = Lock()
# for i in range(10):
#     Thread(target=func1, args=(lock1, lock2,)).start()
# for i in range(10):
#     Thread(target=func2, args=(lock1, lock2,)).start()

# 死锁原因：同时使用了多把锁，并且交替使用
# 解决方案：只使用一把锁，或使用递归锁

