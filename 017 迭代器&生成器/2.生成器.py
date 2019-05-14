#!/usr/bin/env python
# -*- coding:utf-8 -*-
g = (i for i in range(4))
for i in [1, 10]:
    g = (i + j for j in g)
print(list(g))




