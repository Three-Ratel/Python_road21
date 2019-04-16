#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os

"""
1. os.path.exists('path')
"""
# v = os.path.exists('/Users/henry/programme/python/Python_codes/day014 函数补充&模块/1. 带参数的装饰器.py')
# print(v)

"""
2. os.stat('path').st_size 计算单位为字节 byte
os.path.getsize(file)
"""
# v = os.stat('/Users/henry/programme/python/Python_codes/day014 函数补充&模块/1. 带参数的装饰器.py').st_size
# print(v)


"""
3. os.path.abspath('filename')
只能获取本目录下文件的绝对路径
"""

# v = os.path.abspath('codes')
# print(v)


"""
4. os.path.dirname()
"""
# v = os.path.dirname('/Users/henry/programme/python/Python_codes/day014 函数补充&模块/test.py')
# print(v)


"""
5. os.path.join()
"""
# file = 't.txt'
# with open(file, mode='w') as f:
#     pass
# v = os.path.abspath(file)
# print(v)
# os.remove(file)

"""
6. os.path.join(path1, path2)
"""
# file = '2. sys模块.py'
# path = 'user/henry/desktop'
# v = os.path.join(path, file)
# print(v)


"""
7. os.listdir() 指定目录下的第一层文件，默认path = '.'
"""
# v = os.listdir('/Users/henry/programme/python/Python_codes/')
# print(v)


"""
8. os.walk(), 是一个生成器
"""
# v = os.walk('/Users/henry/programme/python/Python_codes/day014 函数补充&模块')
# #a 是目录;b 是目录下的文件夹;c 是目录下的文件
# for a, b, c in v:
#     print('--------')
#     print(a)
#     print('--------')
#     print(b)
#     print('--------')
#     print(c)
#     print('--------')
#     print('===========================')
