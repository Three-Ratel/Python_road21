#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
li = []
i = 0
while i < 101:
    li.append(random.randint(0, 100))
    i += 1

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
i = 1
while i < len(li):
    if i < 1 or li[i - 1] <= li[i]:
        i += 1
    else:
        k = i
        while 0 < k and li[k - 1] > li[k]:
            li[k - 1], li[k] = li[k], li[k - 1]
            k -= 1

print(li)


"""
错误写法
"""
# i = 1
# k = 1
# while i < len(li):
#     i = k
#     print('第一个', i)
#     if i < 1 or li[i - 1] <= li[i]:
#         i += 1
#     else:
#         k = i
#         print('第二个', k)
#         while 0 < i and li[i - 1] > li[i]:
#             li[i - 1], li[i] = li[i], li[i - 1]
#             i -= 1
#
# print(li)







