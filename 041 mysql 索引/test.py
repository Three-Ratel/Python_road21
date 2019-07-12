#!/usr/bin/env python
# -*- coding:utf-8 -*-
# list1 = ['key1','key2','key3']
# list2 = ['1','2','3']
# info = dict(zip(list1,list2))
# print(info)

v = [1, 2, 3, 'welcome', 4, 'hello']
result = filter(lambda x: type(x) == int, v) # 生成新list
print(list(result))
