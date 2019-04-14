#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib
def get_md5(data):
    obj = hashlib.md5('adsfg12fsg'.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()
val = get_md5('123')
print(val)



