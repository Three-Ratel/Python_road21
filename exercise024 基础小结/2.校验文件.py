#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
2.校验大文件的一致性
    基础需求
        普通的文字文件
    进阶需求
        视频或者是图片
"""
import hashlib


file_path1 = '/Users/henry/Movies/Movies/HLBT1.超清中英双字.mp4'
file_path2 = '/Users/henry/Movies/Movies/当幸福来敲门.rmvb'


class Verify(object):
    @staticmethod
    def file_verify(file):
        f = open(file, mode='rb')
        chunk = 1024
        m = hashlib.md5()
        while 1:
            data = f.read(chunk)
            if not data:
                break
            m.update(data)
        f.close()
        return m.hexdigest()


if Verify().file_verify(file_path1) == Verify().file_verify(file_path2):
    print('文件一致')
else:
    print('文件缺失')


def file_verify(file):
    f = open(file, mode='rb')
    chunk = 1024
    m = hashlib.md5()
    while 1:
        data = f.read(chunk)
        if not data:
            break
        m.update(data)
    f.close()


