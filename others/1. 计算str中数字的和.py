#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
任意输入一串文字+数字 计算出来数字的和
如：输入 sdfasd34hs7
"""
s = 'sdf2asd34hs70'
li = []
count = 0
for i in range(len(s)):
    if s[i].isdecimal():
        count += 1
    else:
        li.append(s[i-count:i])
        count = 0
if count != 0:
    li.append(s[-count:])
total = 0

for i in li:
    if len(i) != 0:
        total += int(i.strip())
print(total)



