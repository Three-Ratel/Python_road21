#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib


def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()


v = get_md5('hellodjango')
print(len(v))
print(v)


# def get_hash(data):
#     h = hashlib.sha1()
#     h.update(bytes(data, encoding='utf-8'))
#     s = h.hexdigest()
#     print(s)
#
# get_hash('admin')


