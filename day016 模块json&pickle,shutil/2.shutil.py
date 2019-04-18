#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil

"""
压缩
"""
# shutil.make_archive('test', 'zip', \
#                     os.path.join(os.path.dirname(os.path.dirname(__file__)), 'others'))


"""
解压
"""
# file_path = 'test' + '.zip'
# shutil.unpack_archive(file_path, format='zip', \
#     extract_dir='/Users/henry/programme/python/Python_codes/day016 模块/unpack_test')
#
# shutil.rmtree('unpack_test')


"""
重命名 / 移动
"""
# shutil.move('/Users/henry/programme/python/Python_codes/test.py', 'test.py')
print(os.path.dirname(os.path.dirname(os.path.abspath('test.py'))))