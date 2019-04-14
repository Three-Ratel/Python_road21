#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
只能对str类型数据进行加密
"""
import hashlib
def get_md5(data):
    obj = hashlib.md5('adsfg12fdfghjkldfghj'.encode('utf-8'))
    obj.update(str(data).strip('{}[]()').encode('utf-8'))
    return obj.hexdigest()
val = get_md5(123)
print(val)

# def get_data_md5(data):
#     obj = hashlib.md5('dfghdfg'.encode('utf-8'))
#     obj.update(str(data).strip('[]{}()').encode('utf-8'))
#     v = obj.hexdigest()
#     return v
# v = get_data_md5(123)
# print(v)
