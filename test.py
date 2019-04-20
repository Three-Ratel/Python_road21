#!/usr/bin/env python
# -*- coding:utf-8 -*-

# v = oct(10)
# v = int('11', base=16)
# print(v)

# import keyword
# print(keyword.kwlist)

# li = [1, 2, 4, ['a', 'b']]
# l = li.copy()
# l[3][0] = 3
# l = l.count(4)
# print(li, l)

dict
# li = [1, 2, 3, 4, 5]
# info = {'a': 1, 'b': 2}
# v = info.fromkeys(li, 'hello')
# print(v, info)

set
s1 = {1, 2, 3, 4, 7, 8}
# s.discard(5)
# print(s)

s2 = {1, 2, 3, 4, 5, 6}

# s1.intersection_update(s2)
# print(s1, s2)

# v = s1.isdisjoint(s2)
# print(v)


v = s1.difference(s2)
print(v, s1)
