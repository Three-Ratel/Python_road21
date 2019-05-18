#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
ab = 4
v = getattr(sys.modules[__name__], 'ab')
print(v)
print(sys.modules[__name__])