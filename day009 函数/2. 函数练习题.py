#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  总结  ##################################
'''
1. 函数传输文件名时，需要传输 str 类型(文件具体路径）
2. line = line.strip('\n').split('|'),从左到右操作
3. 如果需要双重甚至多重循环时， 可以考虑先构造一个元素

'''
############################   end   #################################


"""
 示例1 ：请写一个函数，函数计算列表 info = [11,22,33,44,55] 中所有元素的和。
"""
# info = [11, 22, 33, 44]
# def sum_list(li):
#     sum = 0
#     for i in li:
#         sum += i
#     print(sum)
# sum_list(info)


"""
示例2
 让用户输入一段字符串，计算字符串中有多少A，就在文件中写入多少‘echo’
 函数执行过程中遇到return，之后的语句就不会执行
"""
# def get_char_list(arg):
#     if type(arg) is not str:
#         return 'your input content is wrong sort'
#     count = 0
#     for i in arg:
#         if i == 'A':
#             count += 1
#     return count
#
# def write_file(filename, data, count):
#     with open(filename, mode='w', encoding='utf-8') as f:
#         f.write(data * count)
#
# content = input('please input your text: ')
# count = get_char_list(content)
# print(count)
# write_file('c.txt', 'echo', count)





"""
1. 写函数，计算一个list中有多少个数字，打印，有%s个数字
    判断数字：type(a) == int
"""

# def get_num_list(arg):
#     if type(arg) is not list:
#         return -1
#     count = 0
#     for i in arg:
#         if type(i) == int:
#             count += 1
#     print('有%s个数字' % count)
#
#
# li = (1, 2, 3, 'sdaf')
# v = get_num_list(li)
# if v:
#     print(v)


"""
way2
"""
# def get_num_list(arg):
#     count = 0
#     for i in arg:
#         if type(i) == int:
#             count += 1
#     print('有%s个数字' % count)
#
# li = [1, 2, 3, 'sdaf']
# get_num_list(li)
#
#
# # 严谨
# def get_num_list(arg):
#     if type(arg) not in [list]:
#         return -1
#     count = 0
#     for i in arg:
#         if type(i) == int:
#             count += 1
#     print('有%s个数字' % count)
#
#
# li = [1, 2, 3, 'sdaf']
# v = get_num_list(li)
# if v:
#     print(v)



"""
2. 写函数，计算一个列表中偶数索引位置的数据构造成另外一个列表，并返回。
"""

# def new_list(arg):
#     l = arg[::2]
#     return l
#
# li = [1, 2, 3, 123, 4, 65, 'sdaf']
# v = new_list(li)
# print(v)



"""
3. 读取文件，将文件的内容构造成指定格式的数据，并返回。

a.log文件
    alex|123|18
    eric|uiuf|19
    ...
目标结构：
a.  ["alex|123|18","eric|uiuf|19"] 并返回。
b. [['alex','123','18'],['eric','uiuf','19']]
c. [
	{'name':'alex','pwd':'123','age':'18'},
	{'name':'eric','pwd':'uiuf','age':'19'},
]
"""

# def a(filename):
#     li = []
#     with open(filename, mode='r', encoding='utf-8') as v:
#         for line in v:
#             line = line.strip()
#             li.append(line)
#     return li
#
# def b(filename):
#     li = []
#     with open(filename, mode='r', encoding='utf-8') as v:
#         for line in v:
#             line = line.strip()
#             line = line.split('|')
#             li.append(line)
#     return li
#
# def c(filename):
#     li = []
#     with open(filename, mode='r', encoding='utf-8') as v:
#         for line in v:
#             info = {}
#             line = line.split('|')
#             keys = ['name', 'pwd', 'age']
#             for key in keys:
#                 for i in range(len(line)):
#                     info[key] = line[i]
#             li.append(info)
#         return li
#
# va = a('a.log')
# vb = b('a.log')
# vc = c('a.log')
# print(va)
# print(vb)
# print(vc)





