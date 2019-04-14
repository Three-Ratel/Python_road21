#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
str操作可以使用 s.center()
"""

def print_diamond(num):
    s = "*"
    i = 1
    n = 2 * num - 1
    while i < num:
        s1 = s.center(n)
        print(s1)
        s += "**"
        i += 1
    while 1 < i:
        s = s.replace("**", '', 1)
        s1 = s.center(n)
        print(s1)
        i -= 1
print_diamond(100)

# def print_diamond(num):
#     s = "*"
#     n = 2*num-1
#     i = 1
#     while 0 < i < num+1:
#         print((s * (2 * i - 1)).center(n))
#         i += 1
#     else:
#         i = num
#     while 0 < i < num+1:
#         print((s * (2 * i - 1)).center(n))
#         i -= 1
#
# print_diamond(100000)


# def print_diamond(num):
#     s = "*"
#     s1 = " " * len(s)
#     for i in range(1, num + 1):
#         print(s1 * (num - i), s * (2 * i - 1))
#
#     def print_reverse():
#         for i in range(1, num + 1):
#             print(s1 * i, s * (2 * (num - i) - 1))
#     print_reverse()
#
# print_diamond(5)

#
# def print_diamond(num):
#     s = "*"
#     s1 = " " * len(s)
#     i = 1
#     while i <= num:
#         print(s1 * (num - i), s * (2 * i - 1))
#         i += 1
#     else:
#         i = 1
#         while i <= num:
#             print(s1 * i, s * (2 * (num - i) - 1))
#             i += 1
#
# print_diamond(100)
