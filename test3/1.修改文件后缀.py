#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re
import shutil


def modify(file_path):
    patt = re.compile('.*\.png$')
    if not os.path.isdir(file_path): print('文件目录不合法')
    for a, b, c in os.walk(file_path):
        for i in c:
            abs_path = os.path.abspath(a)
            c_path = os.path.join(abs_path, i)
            msg = patt.search(c_path)
            if msg:
                li = msg.group().rsplit('.png', 1)[0] + '.jpg'
                os.rename(c_path, li)


# modify('/Users/henry/programme/python/Python_codes/test3')


"""
把文件夹名称中的day去掉
"""
def modify_in_use(file_path):
    patt = re.compile('^day.*')
    if not os.path.isdir(file_path): print('文件目录不合法')
    for a, b, c in os.walk(file_path):
        for i in b:
            dir_path = os.path.abspath(a)
            abs_path = os.path.join(dir_path,i)
            msg = patt.search(i)
            if msg:
                print(msg.group())
                new_name = os.path.join(dir_path, msg.group().split('day', 1)[1])
                shutil.move(abs_path, new_name)


# modify_in_use('/Users/henry/programme/python/extra_excises')
