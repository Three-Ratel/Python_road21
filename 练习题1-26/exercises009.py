#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  总结  ##################################
'''
1. 切片取值，类型不会发生改变
2. message 标志的妙用，会简化一些代码重复
'''
############################   end   #################################


"""
2. 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回。
"""
# def new_list(arg):
#     if type(arg) not in [list, tuple]:
#         return -1
#     li = []
#     for i in range(0, len(arg), 2):
#         li.append(arg[i])
#     return li
#
# l = (1, 2, 3, 4, 5)
# val = new_list(l)
# print(val)

"""
way2 
"""
# def new_list(arg):
#     if type(arg) not in [list, tuple]:
#         return
#     return list(arg[::2])
#
# # l = (1, 2, 3, 4, 5)
# l = 'asd'
# val = new_list(l)
# print(val)



"""
3. 写函数，判断用户传入的一个对象（字符串或列表或元组任意）长度是否大于5，并返回真假。
"""
# def just_len_n(arg):
#     a = False
#     if len(arg) > 5:
#         a = True
#     return a
#
# l = [1, 2, 3, 4, 5]
# val = just_len_n(l)
# print(val)



"""
4. 写函数，接收两个数字参数，返回比较大的那个数字。
"""
# def compare_big(arg1, arg2):
#     if type(arg1) is not int and type(arg1) is not int:
#         return 'not both args are integer'
#     if arg1 > arg2:
#         a = arg1
#     elif arg1 < arg2:
#         a = arg2
#     return a
#
# v = compare_big('1', 4)
# print(v)


"""
5. 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容根据"*"拼接起来并追加
到一个student_msg文件中。
"""
# def msg_list(name, gender, age, level):
#     age = str(age)
#     li = [name, gender, age, level]
#     li = '*'.join(li)
#     with open('student_msg', mode='a', encoding='utf-8') as f:
#         f.write(li)
#
# name = input('please input your name: ')
# gender = input('please input your gender: ')
# age = input('please input your age: ')
# level = input('please input your education: ')
# msg_list(name, gender, age, level)


"""
6. 写函数，在函数内部生成如下规则的列表  [1,1,2,3,5,8,13,21,34,55…]（斐波那契数列），并返回。
   注意：函数可接收一个参数用于指定列表中元素最大不可以超过的范围。
"""
# def f_num_list(max_num):
#     if type(max_num) is not int:
#         if type(max_num) is str:
#             max_num = int(max_num)
#     if max_num == 0:
#         return []
#     if max_num == 1:
#         return [1]
#
#     li = [1, 1]
#
#     while li[-1] + li[-2] <= max_num:
#         num = li[-1] + li[-2]
#         li.append(num)
#     return li
#
# v = f_num_list(5555555)
# print(v)



"""
7. 写函数，验证用户名在文件 data.txt 中是否存在，如果存在则返回True，否则返回False。
（函数有一个参数，用于接收用户输入的用户名）
   data.txt文件格式如下：
   1|alex|123123
   2|eric|rwerwe
   3|wupeiqi|pppp
"""
# def user_name_list(user_name):
#
#     with open('data.txt', mode='r', encoding='utf-8') as f:
#         for i in f:
#             i = i.strip('\n')
#             i = i.split('|')
#             if name == i[1]:
#                 a = True
#                 return a
#
# name = input('please input user name: ')
# val = user_name_list(name)
# print(bool(val))

