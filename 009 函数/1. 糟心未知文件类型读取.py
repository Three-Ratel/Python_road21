#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
未知文件类型的读取，及取值
按行读取的时，需要strip('\n')
"""

with open('a.txt', mode='w', encoding='gbk') as f:
    s = '你好\n,北京欢迎您'
    f.write(s)

# info = {}
with open('a.txt', mode='rb') as v1:
    v = v1.read()
    print(v)
#     for line in v1:
#         print(line)
#         line = line.strip('\n')
#         key = line[:2]
#         value = line[2:]
#         info[key] = value
# print(info)