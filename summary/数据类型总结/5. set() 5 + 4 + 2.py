#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1. s.add('a')
"""
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.add(5)
# print(s)
# s.add(5)
# print(s)

"""
2. s.discard('a')
"""
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.discard(5)
# print(s)
#
# s.discard(2)
# print(s)


"""
3. s.update()
"""
# # 可以用str ， list， tuple， dict， set， 也可以混合多种类型放入update中

# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s1 = {5, 6, 7, 8, 1, 2, 3}
# s2 = [5, 6, 7, 8, 1, 2, 3]
# s3 = (5, 6, 7, 8, 1, 2, 3)
# s4 = {5: 6, 7: 8, 1: 2}
# s5 = 'asdfgh'
# s.update(s1)
# print(s)
#
#
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.update(s2)
# print(s)
#
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.update(s3)
# print(s)
#
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.update(s4)
# print(s)
#
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.update(s5, 'hello world')
# print(s)

"""
4. s.pop('a')
"""
# s = {1, 'henry', 2, 'echo', 3, 'eliane'}
# s.pop()
# print(s)

"""
5. s.discard()
"""
s = {1, 'henry', 2, 'echo', 3, 'eliane'}
val = s.discard(3)
print(s)
print(val)


"""
6. v.intersection(v1)
"""
# v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
# v2 = {1, 3, 5, 7}
# v = v1.intersection(v2)
# print(v)


"""
7. v.union(v2)
"""
# v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
# v2 = {1, 3, 5, 7}
# v = v1.union(v2)
# print(v)


"""
8. v.difference(v1)
"""
# v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
# v2 = {1, 3, 5, 7}
# v = v1.difference(v2)
# print(v)


"""
9. v.symmetric_difference(v1)
"""
# v1 = {1, 'henry', 2, 'echo', 3, 'eliane'}
# v2 = {1, 3, 5, 7}
# v = v1.symmetric_difference(v2)
# print(v)


"""
10. len(v)
"""
# v = {1, 'henry', 2, 'echo', 3, 'eliane'}
# print(len(v))


"""
11. for循环
"""
# v = {1, 'henry', 2, 'echo', 3, 'eliane'}
# for i in v:
#     print(i)





