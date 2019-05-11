#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
ip 点分二进制，将十进制转为二进制并通过 ， 连接
"""
# ip = '192.168.12.79'
# li = ip.split('.')
# l = []
# for i in li:
#     i = int(i)
#     i = bin(i)
#     i = str(i).replace('0b', '')
#     i = i.rjust(8, '0')
#     l.append(i)
# s = '.'.join(l)
# print(s)


"""
ip转换为二进制拼接在一块，计算对应的十进制值, rjust也可以用zfill()
"""
ip = '192.168.12.79'
li = ip.split('.')
l = ''
for i in li:
    i = str(bin(int(i))).replace('0b', '').rjust(8, '0')
    l += i
s = int(l, base=2)
print(s)
