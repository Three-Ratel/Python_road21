#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# li = [-1, -2, 4, 3, 1]
# l = sorted(li, key=abs, reverse=True)
# print(l)

li = [1, 2, 3, 4, 5]
info = {'a': 1, 'b': 2}
v = info.fromkeys(li, 'hello')
print(v, info)

v = dict.fromkeys(['k1', 'k2'], [])
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)


li = [1,1,2,2,3,4,5]
li = list(set(li))
print(li)

type