#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.你了解生产者模型消费者模型么？如何实现？
"""
# 生产者：一个进程
# 消费者：另一个进程
# 把独立的功能分成多个小功能处理，利用生产者和消费者模型，解决代码之间运行速度的差异，
# 最大化整个程序的运行效率

# 通过中间件，可以使用队列（设置队列长，防止内存溢出），或这使用第三方工具如redis，memcache，kafka，rabbitmq

"""
2.GIL锁是怎么回事?
"""
# GIL：golbal interpreter lock，全局解释器锁
# 进程中有一个垃圾回收线程，用于记录程序中的所有变量引用次数
# 引入GIL，为了解决在同一时刻，只能有一个线程更改变量的引用次数

"""
3.请简述进程和线程的区别？
"""
# 进程：开启、销毁、切换开销大，数据隔离，可以并行
# 线程：开启、销毁、切换开销小，数据共享，不可以并行


"""
4.多进程之间是否能实现数据共享？用哪个模块实现？
"""
# 可以使用中间件，Queue
# 使用multiprocessing 模块中的Queue

"""
5.请继续完成ftp作业：需求5.不同用户家目录不同，且只能访问自己的家目录
"""

"""
生成器练习题
1.读代码猜答案
"""
# g1 = filter(lambda n: n % 2 == 0, range(10))
# g2 = map(lambda n: n * 2, range(3))
# for i in g1:
#     for j in g2:
#         print(i * j)


# 0 0 0
"""
2.以下代码的输出是什么？请给出答案并解释。
请修改multipliers的定义来产生期望的结果。
"""


# def multipliers():
#     return [lambda x: i * x for i in range(4)]
#
#
# print([m(2) for m in multipliers()])

# [6, 6, 6, 6]
