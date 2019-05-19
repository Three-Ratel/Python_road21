#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. 进程池
"""
# import time
# from concurrent.futures import ProcessPoolExecutor
#
# def func(i):
#     time.sleep(0.01)
#     print(i, 'xixihaha')
#     return i
#
#
# pp = ProcessPoolExecutor(5)
# ret = []
# for i in range(100):
#     res = pp.submit(func, i+1)
#     ret.append(res)
# pp.shutdown()
# for i in ret:print(i.result())    # 同步阻塞取结果
# # pp.submit(func, 1000000)

"""
2. 线程池
"""
# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def func(i):
#     time.sleep(0.01)
#     print(i, 'xixihaha')
#     return i
#
#
# pp = ThreadPoolExecutor(5)
# ret = []
# for i in range(100):
#     res = pp.submit(func, i+1)
#     ret.append(res)
# pp.shutdown()
# for i in ret:print(i.result())    # 同步阻塞取结果
# # pp.submit(func, 1000000)

"""
3. map方法
"""
# import time
# from concurrent.futures import ProcessPoolExecutor
#
# def func(i):
#     time.sleep(0.01)
#     print(i, 'xixihaha')
#     return i
#
#
# pp = ProcessPoolExecutor(5)
# res = pp.map(func, range(100))     # res为生成器对象
# pp.shutdown()
# for i in res:print(i)               # 异步取结果


"""
4. 回调函数
"""
# import time
# from concurrent.futures import ProcessPoolExecutor
#
# def func(i):
#     time.sleep(0.01)
#     # print(i, 'xixihaha')
#     return i
#
# def call_back(res):
#     print(res.result())
#
#
# pp = ProcessPoolExecutor(5)
# for i in range(100):
#     res = pp.submit(func, i+1)
#     res.add_done_callback(call_back)






