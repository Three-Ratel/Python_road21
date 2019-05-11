#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1.进制转换
"""
# print(int('0b1111011', base=2))
# print(bin(18))
# print(int('011', base=8))
# print(int('0x12', base=16))
# print(hex(87))


"""
2.python递归的最大深度为1000
"""

"""
3.列举常见的内置函数
"""
# 强制转换：int， bool， str， list， tuple， dict， set
# 输入输出：print， input
# 进制转换：bin， oct， int， hex
# 数学相关：abs， max， min， float， round， divmod， sum
# map/filter/reduce/zip
# 编码相关：chr， ord
# 其他：len， type， id， range， open


"""
4. filter, map, reduce 的作用
"""
# filter，对可迭代对象根据指定标准进行数据筛选
# map，对可迭代对象进行批量的修改
# reduce，对可迭代对象进行指定运算

"""
5. 一行实现9*9乘法表
"""
# [print('%s*%s ' % (i, j,)) if i == j else print('%s*%s ' % (i, j,), end='') \
#  for i in range(1, 10) for j in range(1, i+1)]


"""
6. 什么是闭包
"""
# 闭包就是能够读取其他函数内部变量的函数。
# 在本质上，闭包是将函数内部和函数外部连接起来的桥梁。


"""
7.简述生成器、迭代器、装饰器以及应用场景
"""
# 生成器：主要用于构造大量数据时，为了节省内存空间，使用生成器可以在for 循环的时候一个个的生成数据
# 迭代器：for循环的内部就是通过迭代器的操作来实现
# 装饰器：用于调用其他函数或模块时，可以在其前后进行自定义操作


"""
8.使用生成器编写fib函数，函数声明为fib(max)，输入一个参数max值，是的函数可以这样调用
for i in range(0, 100):
    print(fib(1000))
"""
li = [1, 1]


def func(num=1000):
    a, b = 1, 1
    while a + b < num:
        b = li[-1] + li[-2]
        a = li[-2]
        li.append(b)
        yield b


for i in func():
    print(i)

# for i in range(100):
#     print(fib(1000))




"""
9. 一行代码，通过filter和lambda函数输出以下列表索引为基数对应的元素
"""
# list_a = [12, 213, 22, 2, 2, 2, 22, 2, 2, 32]
# print([i for i in filter(lambda i: i, list_a)])


"""
10. 写一个base62encode函数，把
"""
result = []
li = [str(i) for i in range(10)]


def check_list():
    i = 65
    while i <= 90:
        li.append(chr(i))
        i += 1
    i = 97
    while 97 <= i <= 122:
        li.append(chr(i))
        i += 1


def run():
    while 1:
        num = input('please input a num: ')
        if not num.isdecimal():
            print('your num is wrong')
            continue
        num = int(num)
        return num


def fun(count):
    a, b = divmod(count, 62)
    result.append(li[b])
    if a > 62:
        fun(a)
    else:
        if a:
            result.append(str(a))
        return ''.join(result[::-1])


# check_list()
# v = fun(run())
# print(v)






