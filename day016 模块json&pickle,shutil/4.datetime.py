#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
<class 'datetime.datetime'>
"""
import time
from datetime import datetime, timezone, timedelta


# # 获取datetime格式
# ctime = datetime.now()
# utime = datetime.utcnow()
#
tz = timezone(timedelta(hours=-7))
# print(tz)
# time7 = datetime.now(tz)
#
# print('', ctime, '\n\r', utime, '\n\r', time7)
# print(ctime, type(ctime))


"""
2.datetime 类型转换为str类型
"""
# v1 = datetime.now()
# print(v1, type(v1))
# v2 = v1.strftime('%Y/%m/%d %H:%M:%S')
# print(v2, type(v2))


"""
3.str类型转换为datetime类型
"""
# v1 = '2019-04-18'
# v2 = datetime.strptime(v1, '%Y-%m-%d')
# val = v2 - timedelta(days=40)
# print(v2)
# print(val)

"""
4.time.time() 转换为datetime类型
"""
# ctime = time.time()
# v = datetime.fromtimestamp(ctime, tz)
# print(v)


"""
5. datetime 转换为time.time
"""
v = datetime.now()
val = v.timestamp()
print(val)
print(time.time())










