#!/usr/bin/env python
# -*- coding:utf-8 -*-



############################  总结  ##################################
'''
1. 切片取值，如果结尾值超出索引，则默认取到最后
2. os模块，v = os.path.exists('路径地址')，存在v为 Ture
'''
############################   end   #################################
"""
今日作业
阅读自己
学号 + 1
同学的22题作业，并写在作业下评论，可以是关于：

学习到的知识点。
作业可以优化的部分。
"""
"""
2. 请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先输入
"before"，然后再执行func函数内部代码。
"""


# def wrapper(function):
#     def inner():
#         print('before')
#         return function()
#     return inner
#
#
# @wrapper
# def func():
#     return 100 + 200
#
#
# val = func()


"""
3.请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
"""


# def wrapper(function):
#     def inner():
#         print(11)
#         v = function()
#         print('after')
#         return v
#     return inner
#
#
# @wrapper
# def func():
#     return 100 + 200
#
#
# val = func()



"""
4.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
"""


# def wrapper(function):
#     def inner(*args):
#         v = function(*args)
#         print('after')
#         return v
#     return inner
#
#
# @wrapper
# def func(a1):
#     return a1 + "傻叉"
#
#
# @wrapper
# def base(a1, a2):
#     return a1 + a2 + '傻缺'
#
#
# @wrapper
# def base(a1, a2, a3, a4):
#     return a1 + a2 + a3 + a4 + '傻蛋'

"""
5.请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，
最终返回列表。
"""
# import random
#
#
# def wrapper(function):
#     def inner():
#         li = [function() for i in range(5)]
#         return li
#     return inner
#
#
# @wrapper
# def func():
#     return random.randint(1, 4)
#
#
# result = func()  # 执行5次，并将每次执行的结果追加到列表最终返回给result
# print(result)





"""
6.请为以下函数编写一个装饰器，添加上装饰器后可以实现：执行 read_userinfo 函数时，先检查文件路径是否存在，如果存在
则执行，如果不存在则输入文件路径不存在，并且不再执行read_userinfo函数体中的内容，再将content变量赋值给None。
温馨提示：如何查看一个路径是否存在？import osresult = os.path.exists('路径地址')
# result为True，则表示路径存在。
# result为False，则表示路径不存在。
"""


# def wrapper(function):
#     def inner(path):
#         import os
#         v = function(path) if os.path.exists(path) else None
#         return v
#     return inner
#
#
# @wrapper
# def read_userinfo(path):
#     file_obj = open(path, mode='r', encoding='utf-8')
#     data = file_obj.read()
#     file_obj.close()
#     return data
#
#
# content = read_userinfo('/Users/henry/programme/python/Python_road/day012 函数闭包&模块/good.txt')
# print(content)


"""
7.请为以下user_list函数编写一个装饰器，校验用户是否已经登录，登录后可以访问，未登录则提示：
请登录后再进行查看，然后再给用户提示：系统管理平台【1.查看用户列表】【2.登录】并选择序号。

# 此变量用于标记，用户是否经登录。
#    True,已登录。
#    False,未登录(默认)
"""
# CURRENT_USER_STATUS = False
#
#
# def wrapper(function):
#     def inner():
#         login()
#         if CURRENT_USER_STATUS:
#             function()
#         else:
#             print('请登录后再进行查看')
#     return inner
#
#
# def user_list():
#     """查看用户列表"""
#     for i in range(1, 100):
#         temp = "ID:%s 用户名：老男孩-%s" % (i, i,)
#     print(temp)
#
#
# def login():
#     """登录"""
#     print('欢迎登录')
#     while True:
#         username = input('请输入用户名（输入N退出）：')
#         if username == 'N':
#             print('退出登录')
#             return
#         password = input('请输入密码：')
#         if username == 'alex' and password == '123':
#             global CURRENT_USER_STATUS
#             CURRENT_USER_STATUS = True
#             print('登录成功')
#             return
#         print('用户名或密码错误，请重新登录。')
#
#
# @wrapper
# def run():
#     func_list = [user_list, login]
#     while True:
#         print("""系统管理平台
#         1.查看用户列表；
#         2.登录""")
#         index = int(input('请选择：')) - 1
#         if index >= 0 and index < len(func_list):
#             func_list[index]()
#         else:
#             print('序号不存在，请重新选择。')
#
#
# run()

"""
8. 看代码写结果
"""
# v = [lambda: x for x in range(10)]
# print(v)
# # [lambda:x, lambda:x, lambda:x....] 10个不同
# print(v[0])
# # lambda地址
# print(v[0]())
# # 9


"""
9. 看代码写结果
"""
v = [i for i in range(10, 0, -1) if i > 5]
# v= [10, 9, 8, 7, 6]


"""
10. 看代码写结果
"""
# data = [lambda x: x * i for i in range(10)]  # 新浪微博面试题
# print(data)
# 10个不同lambda表达式地址
# print(data[0](2))
# 19
# print(data[0](2) == data[8](2))
# True


"""
11. 请用列表推导式实现，踢出列表中的字符串，然后再将每个数字加100，最终生成一个新的列表保存。
"""
# data_list = [11, 22, 33, "alex", 455, 'eirc']
# new_data_list = [i + 100 for i in data_list if str(i).isdecimal()]  # 请在[]中补充代码实现。



"""
12. 请使用字典推导式实现，将如果列表构造成指定格式字典.
"""
"""
# 请使用推导式将data_list构造生如下格式：
info_list = {
    1: ('alex', 19),
    2: ('老男', 84),
    3: ('老女', 73)
}
"""
# data_list = [
#     (1, 'alex', 19),
#     (2, '老男', 84),
#     (3, '老女', 73)
# ]

# info_list = {i[0]: (i[1], i[2]) for i in data_list}
# print(info_list)



"""
明日预习
带参数的装饰器


def m1(counter):
    def wrapper(func):
        def inner(*arg, **kwargs):
            return func(*arg, **kwargs)

        return inner

    return wrapper


@m1(5)
def func():
    print(123)


func()

模块http://www.cnblogs.com/wupeiqi/articles/5501365.html

os
sys
time
datetime
"""


