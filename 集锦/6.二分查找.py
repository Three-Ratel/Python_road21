#!/usr/bin/env python
# -*- coding:utf-8 -*-

l = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]

"""
low版本
"""

# start = 0
# def func(l, aim):
#     mid = (len(l)-1)//2
#     if l:
#         if aim > l[mid]:
#             global start
#             start += (mid + 1)
#             func(l[mid + 1:], aim)
#
#         elif aim < l[mid]:
#             func(l[:mid], aim)
#         elif aim == l[mid]:
#             print("bingo", start+mid)
#
#     else:
#         print('找不到')
#
#
# func(l, 66)
# func(l, 6)


"""
升级版
"""


# def search(num, l, start=None, end=None):
#     start = start if start else 0
#     end = end if end is not None else len(l) - 1
#     mid = (end - start)//2 + start
#     if start > end:
#         return None
#     elif l[mid] > num:
#         return search(num, l, start, mid-1)
#     elif l[mid] < num:
#         return search(num, l, mid+1, end)
#     elif l[mid] == num:
#         return mid
#
#
# v = search(66, l)
# print(v)
