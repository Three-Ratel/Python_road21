#!/usr/bin/env python
# -*- coding:utf-8 -*-

v = 'sadfghj'
v1 = v.encode('utf-8')
v2 = v1.decode('utf-8')
print(type(v), v1, type(v1))
print(v2, type(v2))



