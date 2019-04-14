#!/usr/bin/env python
# -*- coding:UTF-8 -*-

text = input('please input your text: ')
index_len = len(text)
index = 0
count = 0
while True:
    if text[index].isdigit():
        count += 1
    index += 1
    if index == index_len:
        break
print(count)



