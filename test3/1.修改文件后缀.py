#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re


def modify(file_path):
    patt = re.compile('.*\.png$')
    if not os.path.isdir(file_path): print('文件目录不合法')
    v = os.walk(file_path)
    for a, b, c in v:
        for i in c:
            abs_path = os.path.abspath(a)
            c_path = os.path.join(abs_path, i)
            msg = patt.search(c_path)
            if msg:
                li = msg.group().rsplit('.png', 1)[0] + '.jpg'
                os.rename(c_path, li)


modify('/Users/henry/programme/python/Python_codes/test3')