#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1.为函数写一个装饰器，在函数执行之后输入after
"""


# def wrapper(function):
#     def inner():
#         function()
#         print('after')
#     return inner
#
#
# @wrapper
# def func():
#     print(123)
#
#
# func()


"""
2.为函数写一个装饰器，把函数的返回值 + 100然后再返回。
"""


# def wrapper(function):
#     def inner():
#         v = function()
#         return v + 100
#     return inner
#
#
# @wrapper
# def func():
#     return 7
#
#
# result = func()
# print(result)



"""
3.为函数写一个装饰器，根据参数不同做不同操作。

- flag为True，则
让原函数执行后返回值加100，并返回。
- flag为False，则
让原函数执行后返回值减100，并返回。
"""

# def x(flag):
#     def wrapper(func):
#         def inner():
#             v = func()
#             v = v + 100 if flag else v - 100
#             return v
#         return inner
#     return wrapper
#
#
#
# @x(True)
# def f1():
#     return 11
#
#
# @x(False)
# def f2():
#     return 22
#
#
# r1 = f1()
# print(r1)

"""
4.写一个脚本，接收两个参数。
- 第一个参数：文件
- 第二个参数：内容
请将第二个参数中的内容写入到
文件（第一个参数）中。
"""
# 执行脚本： python test.py oldboy.txt 你好
# import sys
#
# b = sys.argv[1]
# c = sys.argv[2]
# print(b, c)
# def func(b, c):
#     with open(b, mode='w', encoding='utf-8') as f:
#         f.write(c)
#
# func(b, c)


"""
5.递归的最大次数是多少？
"""
# 1000


"""
6.看代码写结果
"""
# print("你\n好")  # 你换行好
# print("你\\n好") # 你\n好
# print(r"你\n好") # 你\n好



"""
7.写函数实现，查看一个路径下所有的文件【所有】。
"""
# import os
# def ls_dir(path):
#     u = os.walk(path)
#     for items in u:
#         u, v, w = items
#         for i in w:
#             print(i)
# ls_dir('/Users/henry/programme/python/Python_codes/day014 函数补充&模块')


"""
8.写代码
请根据path找到code目录下所有的文件【单层】，并打印出来。
"""
# path = r"D:\code\test.pdf"
# import os
# def ls_single(path):
#     for i in os.listdir(path):
#         print(i)
#     return
#
# ls_single(path)


"""
9.写代码实现【题目1】和【题目2】
"""


# 1.
# def func(a, b, c=1):
    # # way1
    # return func(b, a + b, c+1) if a + b < 4000000 else (b, c)

#     # way2
#     while a + b < 4000000:
#         v = func(b, a+b, c+1)
#         return v
#     else:
#         return b, c
#
#
# v = func(0, 1)
# print(v)


# def func(a, b):
#     v = func(b, a + b) if a + b < 4000000 else b
#     return v
#
#
# v = func(0, 1)
# print(v)

# 2.
# way1
# dicta = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 'hello'}
# dictb = {'b': 3, 'd': 5, 'e': 7, 'm': 9, 'k': 'world'}
# for u, v in dicta.items():
#     if u in dictb:
#         dictb[u] = v + dicta[u]
#     else:
#         dictb[u] = v
# print(dictb)


# # way2
# dictc = {}
# for i in dicta:
#     if i in dictb:
#         dictc[i] = dicta[i] + dictb[i]
#     else:
#         dictc[i] = dicta[i]
# for i in dictb:
#     if i not in dictc:
#         dictc[i] = dictb[i]
# print(dictc)

# # way3
# import copy
# dictc = copy.copy(dicta)
# dictc.update(dictb)
# for i in dicta:
#     if i in dictb:
#         dictc[i] = dicta[i] + dictb[i]
#
# print(dictc)

"""
10.看代码写结果
"""
# [10, 'a']
# [123]
# [10, 'a']

"""
11.实现如下面试题
"""
# 1. ABC
# 2.
# for i in [0, 2, 1, 4, 3]:
#     res[tupleA[i]] = tupleB[i]
# print(res)

# 3.sys.argv 是个列表


# 4.提取ip
# ip = '192.168.0.100'
# li = ip.split('.')


# 5.
# Alist = ['a', 'b', 'c']
# s = ','.join(Alist)
# print(s)


# 6.
# s1 = StrA[-2:]
# s2 = StrA[1]
# s3 = StrA[2]


# 7.
# Alist = [1, 2, 3, 1, 3, 1, 2, 1, 3]
# se = set(Alist)
# li = list(se)
# li.sort()
# print(li)

"""
编程题
"""
# 1.
# import os
#
# print('============================')
# def li_file(dirname):
#     for a, b, c in os.walk(dirname):
#         for i in c:
#             i = os.path.abspath(i)
#             print(i)
#
# li_file('/Users/henry/programme/python/Python_codes/day014 函数补充&模块')


# 2.
# def nice_num():
#     ni_num = []
#     for i in range(2, 1001):
#         total = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 total += j
#         if total == i:
#             ni_num.append(i)
#     return ni_num
# v = nice_num()
# print(v)

# 4.
# alist = [1, 2, 3, 4]
# blist = [1, 2, 4, 3]
#
#
# def func():
#     index = 0
#     count = 0
#     equal = 0
#     l = len(alist)
#     for i in range(l):
#         if alist[i] > blist[i]:
#             index += 1
#         elif alist[i] < blist[i]:
#             count += 1
#         else:
#             equal += 1
#     if index == l:
#         return alist
#     elif count == l:
#         return blist
#     elif equal == l:
#         return alist
#     else:
#         return blist
#
#
# v = func()
# print(v)


# 5. 读取文件etl_log.txt


# with open('el_log.txt', mode='r', encoding='utf-8') as f:
#     for i in f:
#         print(i.strip())




"""
## 明日预习
- time
- datetime
- json
- 等其他
预习：http: // www.cnblogs.com / wupeiqi / articles / 5501365.
html
"""

