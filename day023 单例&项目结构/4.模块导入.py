#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
模块重复导入多次，后面的均无效
"""
import importlib


import test
print('-----------------')
import test


"""
手动重复导入
"""
importlib.reload(test)

