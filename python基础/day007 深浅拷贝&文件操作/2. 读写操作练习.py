#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# 练习1
# 将user中的元素使用_ 连接，并写入'a.txt'
"""
# user = ['alex', 'eric']
# data = '_'.join(user)
# file_object = open('a.txt', mode='w', encoding='utf-8')
# file_object.write(data)
# file_object.close()

"""
# 练习2
# 将user中的元素使用_ 连接，并写入'a.txt'
"""
# user = [
#     {'name': 'alex', 'pwd': '123'},    # alex|123
#     {'name': 'eric', 'pwd': 'olbody'}, # eric|olbody
# ]
# file_object = open('a.txt', mode='w', encoding='utf-8')
# for i in user:
#     data = "%s|%s\n" % (i['name'], i['pwd'])
#     file_object.write(data)
# file_object.close()
#
#
# """
# # 3. 请将a.txt中的文件读取出来并添加到一个列表中 ['alex|123','eric|olbody']
# """
# #方法一
# file = open('a.txt', mode='r', encoding='utf-8')
# result = file.read()
# file.close()
# result = result.strip('\n')
# result = result.split('\n')
# print(result)
#
#
# # 方法二
# result = []
# file_obj = open('a.txt', mode='r', encoding='utf-8')
# for line in file_obj:
#     line = line.strip()
#     result.append(line)
# file_obj.close()
# print(result)
