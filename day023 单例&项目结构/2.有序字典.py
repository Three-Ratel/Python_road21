#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import OrderedDict

info = OrderedDict()
info['k1'] = 123
info['k2'] = 456

print(info, type(info))
print(info.keys(), type(info.keys()))
print(info.items(), type(info.items()))
for i in info.keys():
    print(i)
