#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
练习要求：
    每页展示10条
    根据用户输入的页码，查看
"""

USER_LIST = []
for i in range(1, 836):
    tem = {'name': 'hello-%s' % i, 'email': 'XXXX%s@qq.com' % i}
    USER_LIST.append(tem)

per_page_num = 10
a, b = divmod(len(USER_LIST), per_page_num)
a = a+1 if b else a

num = int(input('please input your num: '))
n = num * per_page_num

if 0 < num <= a:
    data = USER_LIST[n - per_page_num: n]
    for i in data:
        print(i)
else:
    data = '输入有误'
    print(data)




