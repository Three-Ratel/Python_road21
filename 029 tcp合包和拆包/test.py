#!/usr/bin/env python
# -*- coding:utf-8 -*-
import struct

file_name = '肖生克的救赎.rmvb'.encode('utf-8')
first_info = struct.pack('i', len(file_name))

print(struct.unpack('i', first_info)[0])