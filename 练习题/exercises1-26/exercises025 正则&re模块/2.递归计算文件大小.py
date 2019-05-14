#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
二、使用listdir完成计算文件夹大小
"""
import os
path_dir = os.path.dirname(os.path.dirname(__file__))
total = 0
print(path_dir)


def dir_count(path):
    global total
    for i in os.listdir(path):
        path_i = os.path.join(path, i)

        if os.path.isfile(path_i):
            total += os.path.getsize(path_i)
            continue
        dir_count(path_i)


if __name__ == '__main__':
    dir_count(path_dir)
    print(total)



