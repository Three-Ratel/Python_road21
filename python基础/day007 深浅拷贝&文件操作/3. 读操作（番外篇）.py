#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
当文件内容被割裂时，会报错
"""
with open('a.txt', mode='rb') as v:
    v.seek(1)
    obj = v.read(1)
print(obj)



