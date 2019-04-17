#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
v = [1, 2, 3, {"a": 1, "b": 2}, True, "henry", (1,)]
v1 = json.dumps(v)
print(v1, type(v1))
v2 = json.loads(v1)
print(v2, type(v2))



"""
示例：
# import requests
# 需要先安装requests模块：pip install requests
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# print(response.text)
# 获取结构中的所有name字段，使用逗号链接起来，并写入到 catelog.txt 文件中。
[
    {'id': 1, 'name': 'Python', 'hide': False, 'category': 1},
    {'id': 2, 'name': 'Linux运维', 'hide': False, 'category': 4},
    {'id': 4, 'name': 'Python进阶', 'hide': False, 'category': 1},
    {'id': 7, 'name': '开发工具', 'hide': False, 'category': 1},
    {'id': 9, 'name': 'Go语言', 'hide': False, 'category': 1},
    {'id': 10, 'name': '机器学习', 'hide': False, 'category': 3},
    {'id': 11, 'name': '技术生涯', 'hide': False, 'category': 1}
]
"""
# import requests
# import json
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# # response 得到的数据是 .text的文件
# print(response.text)
# v = json.loads(response.text)
# # 反序列化
# print(v)
# data = v['data']
# print(data)
# li = []
# for i in data:
#     li.append(i['name'])
#     s = ','.join(li)
# with open('catelog.txt', mode='w', encoding='utf-8') as f:
#     f.write(s)
