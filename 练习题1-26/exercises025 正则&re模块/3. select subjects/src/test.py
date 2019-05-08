#!/usr/bin/env python
# -*- coding:utf-8 -*-


info1 = {1: {1, 2, 3}, 2: {4, 5, 6}}
info2 = {1: {1, 2, 'haha'}, 2: {4, 5, 6, 'xixi'}}
info1.update(info2)
print(info1)



