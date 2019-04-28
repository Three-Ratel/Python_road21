#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# # 方式1
# content = input('please input ** + **:')
# content1 = content.strip()
# total = int(content1[0]) + int(content1[-1])
# print(total)


# # 方式2
# content = input('please input * + *:')
# index = 0
# total = 0
# while True:
#     char = content[index]
#     if char.isdigit():
#         total += int(char)
#     index += 1
#     if index == len(content) - 1:
#         print(total)
#         break


# 方式3  必须是严格的 23 + 3 结构
content = input('please input * + *:')
val = content.split('+')
total = int(val[0]) + int(val[-1])
print(total)
