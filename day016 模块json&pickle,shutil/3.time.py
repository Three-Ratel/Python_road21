#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time
"""
在终端可实现进度条的打印
"""

# for i in range(10):
#     ctime = time.time()
#     print('%s\r' % ctime, end='')
#     time.sleep(0.1)


ctime = time.time()
local = time.timezone
print(ctime, local)
