#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import hashlib

def get_md5(abs_path):
    obj = hashlib.md5()
    with open(abs_path, mode='rb') as f:
        while True:
            data = f.read(1024)
            if not data: break
            obj.update(data)
    return obj.hexdigest()


# md5 = get_md5('/Users/henry/Movies/Movies/肖申克的救赎.rmvb')


def run():
    while True:
        file1 = input('>>>')
        if os.path.isfile(file1):break

    while True:
        file2 = input('>>>')
        if os.path.isfile(file1): break

    if get_md5(file1) == get_md5(file2):print('md5值一致')
    else:print('md5值一致')

run()