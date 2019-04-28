#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
1.sys.path.append("/root/mods")的作用？
"""
# 把/root/mods路径加入到sys.path中，python解释器可以通过此目录下的自定义的模块
# 使用import到py文件中，python解释器会按照sys.path中的路径进行搜索（list是有序的）

"""
2.字符串如何进行反转？
"""
# s = 'asdfgh'
# s = s[::-1]

"""
3.不用中间变量交换a和b的值。
"""

# a = 1
# b = 2

# a, b = b, a

"""
4. *args和 **kwargs这俩参数是什么意思？我们为什么要用它。
"""
# *args 和 **kwargs是接收不定个数的位置参数和关键字参数
# 为了解决函数重复利用参数不统一的问题

"""
5.函数的参数传递是地址还是新值？
"""
# 传递的是实参的地址

"""
6.看代码写结果：
"""
# my_dict = {'a': 0, 'b': 1}
#
#
# def func(d):
#     d['a'] = 1
#     return d
#
#
# func(my_dict)
# my_dict['c'] = 2
# print(my_dict)

# {'a': 1, 'b': 1, 'c': 2}

"""
7.什么是lambda表达式
"""
# lambda又称为匿名函数，是为了简化代码量，把简单函数用lambda表达式表示


"""
8.range和xrang有什么不同？
"""
# py2同时存在range和xrange，range是一次性在内存中生成一个list
# xrange产生一个"可迭代对象"，通过for循环进行数据的获取
# py3只有range，并且range使用xrange的功能

"""
9."1,2,3"如何变成['1', '2', '3',]
"""
# li = "1,2,3".split(',')
# print(li)

"""
10.['1', '2', '3']如何变成[1, 2, 3]
"""
# l = []
# li = ['1', '2', '3']
# for i in li:
#     l.append(int(i))
# print(l)


"""
11.def f(a, b=[]) 这种写法有什么陷阱？
"""
# 使用默认参数定义函数式，默认值采用可变类型可能会造成可变类型数据被修改

"""
12.如何生成列表[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] ，尽量用一行实现。
"""
# li = [i*i for i in range(1, 101) if i*i < 101]
# print(li)

"""
13.python一行print出1~100偶数的列表, (列表推导式, filter均可)
"""
# print([i for i in range(2, 101, 2)])

# li = filter(lambda x: x % 2 == 0, range(1, 101))


"""
14.把下面函数改成lambda表达式形式
"""


# def func():
#     result = []
#     for i in range(10):
#         if i % 3 == 0:
#             result.append(i)
#     return result

# li = list((lambda: range(0, 11, 3))())
#
# li = [(lambda: i)() for i in range(10) if i % 3 == 0]


# print(li)

"""
15.如何用Python删除一个文件？
"""
# import os
# os.remove('file_path')


"""
16.如何对一个文件进行重命名？
"""
# import os
# os.rename('file_name1', 'file_name2')


"""
17.python如何生成随机数？
"""
import random
# v = random.randint(65, 90)
# print(v)


"""
18.从0 - 99这100个数中随机取出10个数，要求不能重复，可以自己设计数据结构。
"""

# se = set()
# while True:
#     if len(se) == 10:
#         break
#     se.add(random.randint(0, 100))
#
# print(se)

"""
19.用Python实现9 * 9乘法表 （两种方式）
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%s*%s ' % (i, j), end='')
#     print('')

# li = [print('%s*%s ' % (i, j)) if j == i else print('%s*%s ' % (i, j), end='')\
#       for i in range(1, 10) for j in range(1, i + 1)]

li = [[print('%s*%s ' % (i, j)) if j == i else print('%s*%s ' % (i, j), end='')\
      for j in range(1, i+1)] for i in range(1, 10)]


"""
20.请给出下面代码片段的输出并阐述涉及的python相关机制。
"""


# def dict_updater(k, v, dic={}):
#     dic[k] = v
#     print(dic)
#
#
# dict_updater('one', 1)     # {'one': 1}
# dict_updater('two', 2)     # {'one': 1, 'two': 2}
# dict_updater('three', 3, {}) # {'three': 3}
# 因默认参数是可变类型，当不传实参时，就会使用第一次调用的字典

"""
21.写一个装饰器出来。
"""
# def wrapper(func):
#     def inner(*args, **kwargs):
#         v = func()
#         return v
#     return inner


"""
22.用装饰器给一个方法增加打印的功能。
"""
# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('content')
#         v = func()
#         return v
#     return inner()


"""
23. as 请写出log实现(主要功能时打印函数名)
"""


# def log(func):
#     def inner():
#         print('call now()')
#         func()
#     return inner
#
#
# @log
# def now():
#     print("2013-12-25")
#
#
# now()
# 输出call now()2013-12-25


"""
24.向指定地址发送请求，将获取到的值写入到文件中。
"""

# import requests  # 需要先安装requests模块：pip install requests
#
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# print(response.text)

# 获取结构中的所有name字段，使用逗号链接起来，并写入到 catelog.txt 文件中。
"""
[
    {'id': 1, 'name': 'Python', 'hide': False, 'category': 1}, 
    {'id': 2, 'name': 'Linux运维', 'hide': False, 'category': 4}, 
    {'id': 4, 'name': 'Python进阶', 'hide': False, 'category': 1}, 
    {'id': 7, 'name': '开发工具', 'hide': False, 'category': 1}, 
    {'id': 9, 'name': 'Go语言', 'hide': False, 'category': 1},
    {'id': 10, 'name': '机器学习', 'hide': False, 'category': 3}, 
    {'id': 11, 'name': '技术生涯', 'hide': False, 'category': 1}
]
"""
# import requests
# import json
#
#
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# v = json.loads(response.text)
# data = v['data']
# li = []
# for i in data:
#     li.append(i['name'])
#     s = ','.join(li)
# with open('catelog.txt', mode='a+', encoding='utf-8') as f:
#     f.write(s)
# print(s)


"""
25.请列举经常访问的技术网站和博客
"""
# 博客园
# csdn


"""
26.请列举最近在关注的技术
"""
# linux
# git


"""
27.请列举你认为不错的技术书籍和最近在看的书（不限于技术）
"""
# 人类简史
