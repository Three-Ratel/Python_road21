#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import pickle


"""
可转为json的数据中包含中文，让中文完全显示
"""
v = {'k1': 'alex', 'k2': '你好'}
# val = json.dumps(v, ensure_ascii=False)
# print(val, type(val))
#
# val = json.dumps(v)
# print(val, type(val))


"""
json中的 dump 和 load
"""
f = open('a.txt', mode='w', encoding='utf-8')

val = json.dump(v, f)
f.close()
print(val, type(val))

# f = open('a.txt', mode='r', encoding='utf-8')
#
# val = json.load(f)
# f.close()
# print(val, type(val))
#
#
# """
# pickle 只支持python内部转换，几乎支持所有数据转换（socket外）
# """
# v = {'k1': 'alex', 'k2': '你好'}
#
# val = pickle.dumps(v)
# print(val, type(v))
#
# val = pickle.loads(val)
# print(val, type(v))
#
#
# """
# pickle中的dump/load
# """
# f = open('a.txt', mode='wb')
#
# val = pickle.dump(v, f)
# f.close()
# print(val, type(val))
#
# f = open('a.txt', mode='rb')
#
# val = pickle.load(f)
# f.close()
# print(val, type(val))


