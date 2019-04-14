#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1. 取所有key
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# for key in info:
#     print(key)

"""
2. 取所有value
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# for v in info.values():
#     print(v)


"""
3. 取所有key值对
"""
# # 取出的是 tuple 类型
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# for pair in info.items():
#     print(pair)


"""
4. info.get(key, 666)
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# print(info.get(1, 666))
# print(info.get(4, 666))

"""
5. info.pop(key)
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# print(info.pop(1))
# print(info.pop(4))

"""
6. info.update(info1)
"""
# info = {}
# info1 = {1: 'henry', 2: 'echo', 3: 'eliane'}
# info.update(info1)
# print(info)

"""
7. info.setdefault()
"""
# # 查询key，有则取出，没有则添加
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# info.setdefault(4, 'hello')
# print(info)
# # 取出需要赋值给其他变量
# val = info.setdefault(4, 'i hate you')
# print(val)

"""
8. info.popitems()
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# info.popitem()
# print(info)


"""
9. info.clear()
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# info.clear()
# print(info)


"""
10. len(info)
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# print(len(info))

"""
11. index  取值
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# print(info[1])

"""
12. for 循环
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# for i in info:
#     print(i)
# for v in info.values():
#     print(v)
# for pair in info.items():
#     print(pair)


"""
13. 修改
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# info[1] = 'hello'
# print(info)
# info[4] = 'you are smart'
# print(info)

"""
14. 删除
"""
# info = {1: 'henry', 2: 'echo', 3: 'eliane'}
# del info[2]
# print(info)

