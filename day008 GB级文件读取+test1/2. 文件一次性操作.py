#!/usr/bin/env python
# -*- coding:utf-8 -*-

with open('a.txt', mode='r', encoding='utf-8') as v, open('b.txt', mode='w', encoding='utf-8') as v1:
    for i in v.read():
        v1.write(i)
        print(i)



