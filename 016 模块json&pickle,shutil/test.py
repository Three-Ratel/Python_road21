#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 把数据转换为四个字节
import struct
import sys

a = struct.pack('i', 1000)
b = struct.pack('i', 78)
a1 = struct.unpack('i', a)
b1 = struct.unpack('i', b)
print(a)
print(a1[0])



import random
import hashlib
obj = hashlib.md5()
obj1 = hashlib.md5()
obj1.update('eljxldfasdfjk'.encode('utf-8'))
obj.update('eljxldf'.encode('utf-8'))
obj.update('asdfjk'.encode('utf8'))
print(obj.digest())
print(obj1.digest())
print(obj1.hexdigest())
print(sys.modules)
print(sys.argv)



