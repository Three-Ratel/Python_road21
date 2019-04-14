#!/usr/bin/env python
# -*- coding:utf-8 -*-




# with open('b.txt', mode='a+') as f:
#     f.seek(0)
#     f = len(f.readline()s)
#     print(f)




with open('b.txt', mode='a+') as f:
    f.seek(0)
    v = len(f.readline().strip())
    print(v)