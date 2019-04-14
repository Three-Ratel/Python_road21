#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def get_random_data(length=6):
    data = []
    for i in range(length):
        v = chr(random.randint(65, 90)).lower()  # 得到一个随机数
        data.append(v)
    return ' '.join(data)


code = get_random_data(6)
print(code)
user_verify = (input('please input the code of pic: ')).lower()
if ' '.join(user_verify) == code:
    print('True')
else:
    print('Flase')




