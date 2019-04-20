#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################  总结  ##################################
'''
1. range()是range类
2. return 1， 2， 3 返回的是元组
3. 注意：函数类似于变量，func代指一块代码的内存地址。
4. a = ('b', 3, 4)*2 ，tuple里面的数据重复2次. list 和 tuple都可以
'''
############################   end   #################################

"""
1.写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
"""
# def get_sum(*args):
#     for i in args:
#         if type(i) is not int:
#             return
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# val = get_sum(*range(101))
# print(val)


"""
2.看代码写结果
"""
# def func():
#     return 1, 2, 3
#
# val = func()
# print(type(val) == tuple)     # True
# print(type(val) == list)      # Flase


"""
3.看代码写结果
"""


def func(*args, **kwargs):
    pass


# a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# d. 如执行 
# func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
# f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？


# a. func(*[1, 2, 3, 4])
# b. func([1, 2, 3, 4], [11, 22, 33])
# c. func(*[[11, 22], 33], **{'k1': 'v1', 'k2': 'v2'})
# d. args: ('武沛齐', '金鑫', '女神')
#     kwargs : {}
# e. args: ({'武沛齐','金鑫','女神'}, [11,22,33])
#     kwargs : {}
# f. args: ('武沛齐','金鑫','女神',[11,22,33])
#     kwargs : {'k1':'栈'}


"""
4.看代码写结果
"""
def func(name, age=19, email='123@qq.com'):
    pass


# a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？

# a. 可行， name='alex', age=19, email='123@qq.com'
# b. 可行， name='alex', age=20, email='123@qq.com'
# c. 可行， name='alex', age=20, email=30
# d. 可行， name='alex', age=19, email='x@qq.com'
# e. 可行， name='alex', age=99, email='x@qq.com'
# f. 不可行，位置传参必须在关键字传参之前
# g. 不可行，位置传参必须在关键字传参之前



"""
5.看代码写结果
"""
# def func(users, name):
#     users.append(name)
#     return users
#
# result = func(['武沛齐', '李杰'], 'alex')
# print(result)

# ['武沛齐', '李杰', 'alex']


"""
6.看代码写结果
"""
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     return "%s 是什么玩意？" % (arg,)
#
#
# val = func('你')
# data = bar(val)
# print(data)

# 你你 是什么玩意？




"""
7.看代码写结果
"""
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     msg = "%s 是什么玩意？" % (arg,)
#     print(msg)
#
#
# val = func('你')
# data = bar(val)
# print(data)

# 你你 是什么玩意？
# None



"""
8.看代码写结果
"""
# v1 = '武沛齐'
#
# def func():
#     print(v1)
#
#
# func()
# v1 = '老男人'
# func()

# 武沛齐
# 老男人


"""
9.看代码写结果
"""

# v1 = '武沛齐'
#
#
# def func():
#     v1 = '景女神'
#
#     def inner():
#         print(v1)
#
#     v1 = '肖大侠'
#     inner()
#
#
# func()
# v1 = '老男人'
# func()

# 肖大侠
# 肖大侠


"""
10.看代码写结果【可选】
"""
# def func():
#     data = 2 * 2
#     return data
#
#
# new_name = func
# val = new_name()
# print(val)

# 注意：函数类似于变量，func代指一块代码的内存地址。
#
# 4


"""
11.看代码写结果【可选】
"""

# def func():
#     data = 2 * 2
#     return data
#
#
# data_list = [func, func, func]
# for item in data_list:
#     v = item()
#     print(v)

# 注意：函数类似于变量，func代指一块代码的内存地址。

# 4
# 4
# 4

"""
12.看代码写结果（函数可以做参数进行传递）【可选】
"""
# def func(arg):
#     arg()
#
# def show():
#     print('show函数')
#
#
# func(show)

# show函数




