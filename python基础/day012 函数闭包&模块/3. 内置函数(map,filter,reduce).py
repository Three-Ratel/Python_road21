#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
map操作的 func 是一个函数 v 必须是可迭代
"""
# v = [11, 22, 33]
# def func(arg):
#   return arg + 100
#
# result = map(func, v) # 将函数的返回值添加到空list中[111, 122, 133]
# print(list(result))
#
# # 使用lambda 改写
# result = map(lambda x: x+100, v)
# print(result)		# py2直接返回
# print(list(result)) # py3会返回一个object，可用list()查看

"""
filter
"""
# v = [1, 2, 3, 'welcome', 4, 'hello']
# result = filter(lambda x: type(x) == int, v)  # 生成新list
# print(list(result))


"""
reduce (py2中是内置函数，py3被移到别处
    reduce 有两个参数，第一次取前两个值，下次把函数return 值作为x，再继续取1个值作为y
"""
# import functools
# v = [1, 2, 3, 4, 's']
# result = functools.reduce(lambda x, y: x+y, v)
# print(result)


"""
zip
"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)     # 打包为元组的列
print(list(zip(a, c)))
# 元素个数与最短的列表一致
print(list(zip(*zipped)))
# 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
