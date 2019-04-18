#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
sys 模块的使用
"""
import sys

# 1.sys.getrefcount()

# a = [1, 2, 3]
# b = a
# v = sys.getrefcount(a)
# print(v)


# 2.sys.getrecursionlimit()

# count = sys.getrecursionlimit()
# print(count)


# 3.sys.stdout.write('hello') 不会换行

# v = sys.stdout.write('hello')
# v = sys.stdout.write('how are you')


# 4.sys.path
# for i in sys.path:
#     print(i)


# 5.sys.argv() / sys.path() / shutil
# path = 'test/test.txt'
# with open(path, mode='w') as f:
#     pass
# print(sys.argv)
# sys.argv.append(path)
# print(sys.argv)





# import shutil
#
# shutil.rmtree(path)




