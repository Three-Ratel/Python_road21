#!/usr/bin/env python
# -*- coding:utf-8 -*-

import copy
v1 = 34567
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(id(v1), id(v2), id(v3))



