#!/usr/bin/env python
# -*- coding:UTF-8 -*-
s = "13intdkjf"
count = 0
while count < len(s):
    if s[count].isdigit():
        print(s[count].isdigit())
        count += 1
        if s[count].isdigit():
            continue
        s1 = s[0:count]
        print(s1)


ss1 = input('计算h和H的个数: ')
index2 = 0
count1 = 0
ss2 = ss1.lower()
while index2 < len(ss1):
    if ss2[index2] == 'h':
        count1 += 1
    index2 += 1
print(count1)