#!/usr/bin/env python
# -*- coding:utf-8 -*-

chars_list = ['alex', 'echo', 'henry']
content = input('please input your content: ')

message = True
for i in chars_list:
    if i in content:
        message = False
        break
if message:
    print(content)
else:
    print('content includes senstive words')



