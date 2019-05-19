#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. gevent模块实现协程
"""
# import gevent
# from gevent import queue
#
#
# def func1():
#     print('in func1')
#     gevent.sleep(0.1)
#     print('in func1')
#
#
# def func2():
#     print('in func2')
#     gevent.sleep(0.1)
#     print('in func2')
#
#
# g1 = gevent.spawn(func1)
# g2 = gevent.spawn(func2)
# g1.join()

"""
2. gevent 实现socket
"""
# import socket
# import gevent
# from gevent import monkey
#
# monkey.patch_all()
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
3. asynciom模块
"""
# # 启动一个任务
# import asyncio
#
# async def func():
#     print(123)
#     await asyncio.sleep(1)
#     print(456)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())


"""
3.1 启动多个任务
"""

# import asyncio
#
# async def func(i):
#     print(i)
#     await asyncio.sleep(1)
#     print('我是%s' % i)
#
#
# loop = asyncio.get_event_loop()
# wait_obj = asyncio.wait([func(1), func(2), func(3)])
# loop.run_until_complete(wait_obj)

"""
3.2 同步获取返回值
"""
# import asyncio
#
# async def func(i):
#     print(i)
#     await asyncio.sleep(1)
#     print('我是%s' % i)
#     return i
#
# loop = asyncio.get_event_loop()
# t1 = loop.create_task(func(1))
# t2 = loop.create_task(func(2))
# t3 = loop.create_task(func(3))
# task_l = [t1, t2, t3]
# wait_obj = asyncio.wait(task_l)
# loop.run_until_complete(wait_obj)
# for i in task_l: print(i.result())

"""
3.3 异步取返回值
"""
# import asyncio
#
#
# async def func(i):
#     await asyncio.sleep(10 - i)
#     return i
#
#
# async def main():
#     task_l = []
#     for i in range(10):
#         task = asyncio.ensure_future(func(i))
#         task_l.append(task)
#     for ret in asyncio.as_completed(task_l):
#         ret = await ret
#         print(ret)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
