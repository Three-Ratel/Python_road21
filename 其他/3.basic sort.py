#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
导入随机数列
"""
"""
随机数，会重复
"""
# from random_list import func
# li = func(0, 50, 20)

"""
逆序数列
"""
li = [i for i in range(20, 0, -1)]

"""
查看要排序的数列
"""
# li = [i for i in range(20)]
print(li)


"""
# way1
i = 0
while i < len(li):
    if i < 0 or li[i - 1] <= li[i]:
        i += 1
    else:
        li[i - 1], li[i] = li[i], li[i - 1]
        i -= 1

print(li)
"""


"""
# way2:improve
"""
# i = 1
# while i < len(li):
#     if i < 1 or li[i - 1] <= li[i]:
#         i += 1
#     else:
#         k = i
#         while 0 < k and li[k - 1] > li[k]:
#             li[k - 1], li[k] = li[k], li[k - 1]
#             k -= 1
#
# print(li)


"""
繁琐写法
"""
# i = 1
# k = 1
# while i < len(li):
#     i = k
#     if i < 1 or li[i - 1] <= li[i]:
#         i += 1
#         k = i
#     else:
#         while 0 < i and li[i - 1] > li[i]:
#             li[i - 1], li[i] = li[i], li[i - 1]
#             i -= 1
#
# print(li)


"""
冒泡排序
"""
# class Bubble(object):
#
#     def __call__(self, *args, **kwargs):
#         for i in range(len(li)-1):
#             for i in range(len(li)-1):
#                 if li[i] > li[i+1]:
#                     li[i], li[i+1] = li[i+1], li[i]
#         return li
#
#
# li = Bubble()()
# print(li)


"""
冒泡排序改进：提前终止的bubble
"""
# def swap(li):
#     i = 1
#     sorted = True
#     while i < len(li):
#         if li[i-1] > li[i]:
#             sorted = False
#             li[i - 1], li[i] = li[i], li[i - 1]
#         i += 1
#     return sorted
#
#
# def bubble(li):
#     j = len(li) - 1
#     while j:
#         j -= 1
#         if swap(li):
#             break
#     print('哈哈，我是j，看我是不是0哦', 'j =', j)
#
#
# bubble(li)
# print(li)


"""
冒泡排序改进：提前终止的bubble + 脏位判断
"""
last = 0
def swap(li):
    i = 1
    global last
    print(last, end=' ')
    sorted = True
    while i < len(li) - last:
        if li[i-1] > li[i]:
            sorted = False
            li[i - 1], li[i] = li[i], li[i - 1]
            last = i
        i += 1
    return sorted


def bubble(li):
    j = len(li) - 1
    while j:
        j -= 1
        swap(li)
    print('')
    print('哈哈，我是j，看我是不是0哦', 'j =', j)


bubble(li)
print(li)



"""
验证
"""
flag = '正确'
for i in range(len(li)-1):
    if li[i] > li[i+1]:
        flag = '错误'
        break

print(flag, li[i])
