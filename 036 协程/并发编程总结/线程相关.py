#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. 开启线程
"""
# import os
# from threading import Thread
#
# def func(i):
#     print('thread%s' % i, os.getpid())
#
# t_l = []
# for i in range(100):
#     t = Thread(target=func, args=(i+1,))
#     t.start()
#     t_l.append(t)
# for t in t_l:t.join()
# print('main', os.getpid())

"""
2. 面向对象启动线程
"""
# import os, time
# from threading import Thread
#
# class Mythread(Thread):
#
#     def __init__(self, i):
#         self.i = i
#         super().__init__()
#
#     def run(self):
#         print(self.i, self.ident)
#         time.sleep(0.1)
#
#
# for i in range(100):
#     Mythread(i).start()
# print(os.getpid())


"""
3.线程的其他方法，enumerate，active_count，current_thread
"""
# import os, time
# from threading import Thread, current_thread,enumerate, active_count
#
#
# def func(i):
#     time.sleep(0.01)
#     print('thread%s' % i, current_thread())
#
#
# t_l = []
# for i in range(100):
#     t = Thread(target=func, args=(i + 1,))
#     t.start()
#     t_l.append(t)
# for t in t_l: t.join()
# print(enumerate(),'\n', active_count())

"""
4. 守护线程
"""
# import time
# from threading import Thread
#
#
# def son():
#     while True:
#         time.sleep(0.5)
#         print(123)
#
#
# def son2():
#     for i in range(5):
#         time.sleep(1)
#
#
# t = Thread(target=son)
# t.daemon = True
# t.start()
# Thread(target=son2).start()
# time.sleep(3)

"""
5. 线程实现，单例模式 + Lock
"""
# import time
# from threading import Thread
#
#
# class Singleton:
#     __instance = None
#     from threading import Lock
#     lock = Lock()
#
#     def __new__(cls, *args, **kwargs):
#         with cls.lock:
#             if not cls.__instance:
#                 time.sleep(0.01)
#                 cls.__instance = object.__new__(cls)
#             return cls.__instance
#
# li = []
# def run():
#     li.append(id(Singleton()))
#
# t_l = []
# for i in range(1000):
#     t = Thread(target=run)
#     t.start()
#     t_l.append(t)
# for t in t_l:t.join()
# flag = True
# for i in range(len(li)-1):
#     if li[i] != li[i+1]:flag = False
# print(flag)



