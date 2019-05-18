#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
线程部分：读程序
1、程序从flag a执行到falg b的时间大致是多少秒？
"""

# import threading
# import time
#
#
# def _wait():
#     time.sleep(60)
#
#
# # flag a
# t = threading.Thread(target=_wait, daemon=False)
# t.start()
# # flag b
#
# # 立即执行结束

"""
2、程序从flag a执行到falg b的时间大致是多少秒？
"""
# import threading
# import time
#
#
# def _wait():
#     time.sleep(60)
#
#
# # flag a
# t = threading.Thread(target=_wait, daemon=True)
# t.start()
# # flag b

# 立即执行结束


"""
3、程序从flag a执行到falg b的时间大致是多少秒？
"""
# import threading
# import time
#
#
# def _wait():
#     time.sleep(60)
#
#
# # flag a
# t = threading.Thread(target=_wait, daemon=True)
# t.start()
# t.join()
# # flag b

# 60s

"""
4、读程序，请确认执行到最后number是否一定为0
"""
# import threading
#
# loop = int(1E7)
#
# def _add(loop: int = 1):
#     global number
#     for _ in range(loop):
#         number += 1
#
#
# def _sub(loop: int = 1):
#     global number
#     for _ in range(loop):
#         number -= 1
#
#
# number = 0
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# print(number)

# 不一定为0

"""
5、读程序，请确认执行到最后number是否一定为0
"""
import threading

loop = int(1E2)


def _add(loop: int = 1):
    global number
    for _ in range(loop):
        print(_)
        number += 1


# def _sub(loop: int = 1):
#     global number
#     for _ in range(loop):
#         number -= 1


number = 0
ta = threading.Thread(target=_add)
# ts = threading.Thread(target=_sub, args=(loop,))
ta.start()
ta.join()
# ts.start()
# ts.join()
# print(number)

# 为0

"""
7、读程序，请确认执行到最后number的长度是否一定为1
"""
# import threading,time
#
# loop = int(1E7)
#
#
# def _add(loop: int = 1):
#     global numbers
#     for _ in range(loop):
#         numbers.append(0)
#
#
# def _sub(loop: int = 1):
#     global number
#     while not numbers:
#         time.sleep(1E-8)
#     for _ in range(loop):
#         numbers.pop()
#
#
# numbers = [0]
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# print(len(numbers))

# 为1



"""
8、读程序，请确认执行到最后number的长度是否一定为1
"""
# import threading, time
#
# loop = int(1E7)
#
#
# def _add(loop: int = 1):
#     global numbers
#     for _ in range(loop):
#         numbers.append(0)
#
#
# def _sub(loop: int = 1):
#     global numbers
#     while not numbers:
#         time.sleep(1E-8)
#     for _ in range(loop):
#         numbers.pop()
#
#
# numbers = [0]
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# print(len(numbers))

# 为1


"""
协程
1、什么是协程？常用的协程模块有哪些？
"""
# 协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。
# 一句话说明什么是协程：协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的
# 常用模块：gevent 和 asyncio

"""
2、协程中的join是用来做什么用的？它是如何发挥作用的？
"""
# 协程中，join用来阻塞知道任务执行结束

"""
3、使用协程实现并发的tcp server端
"""
# import gevent
# from gevent import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1', 9000))
# sk.listen()
#
#
# def chat(con):
#     while True:
#         msg = con.recv(1024).decode('utf-8')
#         con.send(msg.upper().encode('utf-8'))
#
#
# while True:
#     con, _ = sk.accept()
#     gevent.spawn(chat, con)


"""
4、在一个列表中有多个url，请使用协程访问所有url，将对应的网页内容写入文件保存
"""
# import requests
# import gevent
# from gevent.queue import Queue
#
# def get_page(url, q):
#     response = requests.get(url)
#     q.put({'url': url, 'response': response.text})
#
#
# def write(q):
#     with open('content', 'a+', encoding='utf-8') as f:
#         while True:
#             dic = q.get()
#             if not dic:
#                 break
#             print(dic['url'])
#             f.write(str(dic) + '\n')
#
#
# q = Queue()
# g_l = []
# url_l = ['https://www.baidu.com', 'https://www.cnblogs.com/henryw/', 'https://www.cnblogs.com']
# for i in url_l:
#     g = gevent.spawn(get_page, i, q)
#     g_l.append(g)
#
# ret = gevent.spawn(write, q)
# gevent.joinall(g_l)
# q.put(None)


"""
综合
1、进程和线程的区别
"""
# 进程：os分配资源的最下单位，创建、销毁和切换开销较大，至少有一条线程，可以实现并发后并行
# 线程：cpu执行的最小单位，创建、销毁和切换开销较小，不能脱离进程存在，只能实现并发
"""
2、进程池、线程池的优势和特点 
"""
# 进程池、 线程池
# 预先开启固定个数的进程数，当任务来临时，直接提交给开好的进程，让这个进行执行，从而减轻了os调度的负担
# 节省了进程、线程创建和销毁的时间


"""
3、线程和协程的异同?
"""
# 进程：os分配资源的最下单位，创建、销毁和切换开销较大，至少有一条线程，可以实现并发后并行
# 线程：cpu执行的最小单位，创建、销毁和切换开销较小，不能脱离进程存在，只能实现并发

"""
4、请简述一下互斥锁和递归锁的异同？
"""
# 互斥锁：在同进程、线程中不能连续acquire多次，每次使用完后需要进行release
# 递归锁：在同进程、线程中可以连续acquire多次，acquire次数要与release次数相等

"""
5、请列举一个python中数据安全的数据类型？
"""
# queue

"""
6、 Python中如何使用线程池和进程池
"""
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# th = ThreadPoolExecutor(20)
# th.submit(func, arg1, arg2...)
# pp = ProcessPoolExecutor(20)
# pp.submit(func, arg1, arg2...)

"""
7、简述 进程、线程、协程的区别 以及应用场景？
"""
# 进程：os分配资源的最下单位，创建、销毁和切换开销较大，至少有一条线程，可以实现并发后并行
# 线程：cpu执行的最小单位，创建、销毁和切换开销较小，不能脱离进程存在，只能实现并发
# 协程：需要时间时间循环的第三方进行协程间的切换，切换开销小

# 场景：
# 进程：多个不同的业务，需要并发
# 线程：高并发，有io操作
# 协程：高并发，有io操作
"""
8、什么是并行，什么是并发？
"""
# 并行：多个进程在多个cpu上在同一时间同时运行
# 并发：多个进程占用共享同一cpu，按照时间分片交替执行
