#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 示例：用户登陆
users = []
for i in range(0, 3):
    name = input('录入用户信息:')
    users.append(name)
print(users)

# 用户校验

username = input('输入用户名:')
password = input('输入密码:')
for item in users:
    result = item.split(',')
    user = result[0]
    pwd = result[1]
    if user == username and pwd == password:
        print('登陆成功')
        break

# print('用户名或密码错误')





