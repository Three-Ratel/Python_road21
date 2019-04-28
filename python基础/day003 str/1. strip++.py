#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
默认可以去掉 \n , \t , 空格
"""
# s = 'asdfgh\t'
# print('---------')
# print('-->', s, '<--')
# print('---------')
# s = s.strip()
# print('-->', s, '<--')
# print('---------')


"""
可以去掉任意指定字符,
只要找到某一字符，会从头重新在匹配一遍
"""
s = 'abcdefghijk'
s = s.strip('bak')
print(s)

