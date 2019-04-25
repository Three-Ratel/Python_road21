#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
11. 实现一个装饰器，限制该函数调用频率，如10s 一次
"""
# import time
# def wrapper(func):
#     def inner():
#         v = func()
#         time.sleep(10)
#         return v
#
#     return inner
#
# @wrapper
# def function():
#     print('hello')
#
#
# while 1:
#     function()


"""
12. 实现一个装饰器，通过一次调用函数重复执行5次
"""
# def outside(num):
#     def wrapper(func):
#         def inner():
#             v = []
#             for i in range(num):
#                 v.append(func())
#             return v
#         return inner
#     return wrapper
#
# @outside(5)
# def func():
#     print('hello, Python')
#
# func()


"""
13. python一行print出1-100偶数list，（list推导式，filter均可）
"""
# print([i for i in range(1, 101) if i % 2 == 0])
# print(list(filter(lambda i: i,  range(2, 101, 2))))
# print(list(filter(lambda i: i if i % 2==0 else None,  range(1, 101))))


"""
14.解释生成器与函数的不同，并实现和简单使用generator
"""
# 1.语法上和函数类似：生成器函数和常规函数几乎一模一样的,他们都是使用def语句进行定义，
# \区别在于，生成器使用yield语句返回一个值，而常规函数使用return语句返回一个值
# 2.自动实现迭代器的协议：对于生成器，python自动实现迭代器协议，所以我们可以调用它的next
# \方法，并且在没有值返回的时候，生成器自动生成Stopltwration异常
# 3.状态挂起，生成器使用yield语句返回一个值.yield语句挂起该生成器函数的状态，保留足够的信息，
# \方便之后离开的地方继续执行

# print((i for i in range(100)))


"""
15. [i % 2 for i in range(10)] 和(i % 2 for i in range(10))
"""
# print([i % 2 for i in range(10)])
# print(list(i % 2 for i in range(10)))

"""
16. map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
"""
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


"""
17. python定义函数时，如何书写可变参数和关键字参数
"""
# def func(*args, **kwargs):
#     pass


"""
18. Python3.5中enumerate的意思是什么
"""
# 枚举，在使用enumera函数时，至少需要传入一个可迭代对象,通过迭代一一取出同时为
# \每个元素添加一个序号，默认为0开始，也可以在传参时指定
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
# 等价于
# for i in enumerate(range(100)):
#     print(i)


"""
19. 说说python中的装饰器，迭代器的用法，描述dict的item方法与iteritems方法的不同
"""
# 装饰器：为了在调用一些模块或函数时，在其前后进行自定义化操作时使用
# 迭代器：主要用于可迭代对象，可以通过迭代器一一获取可迭代对象中的元素
# dict.items 是一个list
# dict.iteritems 是一个<type 'dictionary-itemiterator'>的迭代器


# info = {'1': 1, '2': 2, '3': 3}
# val = info.iteritems()
# help (val)
# print(type(val))
# for i, j in val:
#     print i, j


"""
20. 是否使用过functools中的函数，其作用是什么
"""
# functools.partial
# functools.reduce
#


