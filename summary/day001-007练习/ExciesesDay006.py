#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day006  ##################################
'''
1. None 也可以作为dict 的key 或者 set 的 元素
2. None 的类型为 NoneType， 但数据类型中不识别 例如：11题
'''
#############################   end   ##################################

"""
1.列举你了解的字典中的功能（字典独有）。
"""
# 1. info.keys()
# 2. info.values()
# 3. info.items()
# 4. info.get('key', 666)
# 5. info.update(info2)
# 6. info.pop('key')



"""
2.列举你了解的集合中的功能（集合独有）。
"""
# 1. v.add('a')
# 2. v.update(v2)
# 3. v.discard('a')
# 4. v.intersection(v2)
# 5. v.union(v2)
# 6. v.difference(v2)
# 7. v.symmetric_difference(v2)

"""
3.列举你了解的可以转换为
布尔值且为False的值。
"""
# None, 0, '', [], (), {}, set()

"""
4.请用代码实现
info = {'name': '王刚蛋', 'hobby': '铁锤'}

- 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出。
- 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出（如果key不存在，则获取默认“键不存在”，并输出）。
注意：无需考虑循环终止（写死循环即可）
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤'}
# while True:
#     s = input('please input a string: ')
#     if s in info:
#         print(info[s])
#     else:
#         print('key不存在')


"""
5.请用代码验证"name"是否在字典的键中？

info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18',..
.100
个键值对}
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# if 'name' in info:
#     print('name is in info')
# else:
#     print('not in')


"""
6.请用代码验证"alex"是否在字典的值中？

info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18',..
.100
个键值对}
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# if 'ales' in info.values():
#     print('alex is in info')
# else:
#     print('not in')



"""
7.有如下
v1 = {'武沛齐', '李杰', '太白', '景女神'}
v2 = {'李杰', '景女神}

      - 请得到 v1 和 v2 的交集并输出
      - 请得到 v1 和 v2 的并集并输出
      - 请得到 v1 和 v2 的 差集并输出
      - 请得到 v2 和 v1 的 差集并输出
"""
# v1 = {'武沛齐', '李杰', '太白', '景女神'}
# v2 = {'李杰', '景女神'}
# v3 = v1.intersection(v2)
# print(v3)
# v3 = v1.union(v2)
# print(v3)
# v3 = v1.difference(v2)
# print(v3)
# v3 = v2.difference(v1)
# print(v3)


"""
8. 循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
"""
# li = []
# while True:
#     content = input('please input your content(N/n stop): ')
#     if content.lower() == 'n':
#         break
#     li.append(content)
# print(li)



"""
9.循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
"""
# s = set()
# while True:
#     content = input('please input your content(N/n stop): ')
#     if content.lower() == 'n':
#         break
#     s.add(content)
# print(s)

"""
10.写代码实现
# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，
    则添加到v1中。（如果输入N或n则停止循环）
"""
# v1 = {'alex', '武sir', '肖大'}
# v2 = []
#
# while True:
#     content = input('please input your content(N/n stop): ')
#     if content.lower() == 'n':
#         break
#     if content in v1:
#         v2.append(content)
#     else:
#         v1.add(content)
# print(v1, v2)


"""
11.判断以下值那个能做字典的key ？那个能做集合的元素？
- 1
- -1
- ""
- None
- [1, 2]
- (1,)
- {11, 22, 33, 4}
- {'name': 'wupeiq', 'age': 18}
"""
# li = [1, -1, "", None, [1, 2],  (1,), {11, 22, 33, 4}, {'name': 'wupeiq', 'age': 18}]
# l2 = []
# for i in li:
#     if type(i) not in [list, dict, set]:
#         l2.append(i)
# for i in l2:
#     if i == "":
#         i = '""'
#     print(i)


"""
12. is 和 == 的区别？
"""
# is 判断两个变量的内存地址是否一致
# == 判断两个变量的值是否一样

"""
13.type使用方式及作用？
"""
# type(v)


"""
14.id的使用方式及作用？
"""
# id(v)



"""
15.看代码写结果并解释原因
"""

# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)      # True ,v1 和v2 内容上是一样的
# print(result2)      # False,v2 是新的变量，地址与v1 不同


"""
16.看代码写结果并解释原因
"""
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)      # True
# print(result2)      # True




"""
17.看代码写结果并解释原因
print(v2)
"""
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2)   # v1修改了内存中的值，v2 也随之改变




"""
18.看代码写结果并解释原因
"""
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
#
# v1 = "人生苦短，用毛线Python"
#
# print(v2)   # [1, 2, 3, 4, '人生苦短，我用Python']对于v2，内存中的值并没有变化
#




"""
19.看代码写结果并解释原因
"""

# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
#
# info.append(9)
# print(userinfo)   # 所有的info都发生变化
#
# info = "题怎么这么多"
# print(userinfo)     # 所有info和上面保持一致



"""
20.看代码写结果并解释原因
"""
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo) # info 和userinfo所有值都发生改变





"""
21.看代码写结果并解释原因
"""
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)       # 所有info都发生改变





"""
22.看代码写结果并解释原因
"""
# info = [1, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1] = "是谁说Python好学的？"
#
# print(user_list)    # info修改了值，所有的info值都发生改变




"""
23.
看代码写结果并解释原因
"""
# data = {}
# for item in range(10):
#     data['user'] = item
# print(data)     # 会输出1个值





"""
24.看代码写结果并解释原因
"""
# data_list = []
# data = {}
# for item in range(10):
#     data['user'] = item
#     data_list.append(data)
# print(data_list)     # 会输出10个一样的值





"""
25.看代码写结果并解释原因
"""
# data_list = []
# for item in range(10):
#     data = {}
#     data['user'] = item
#     data_list.append(data)
# print(data_list)   # 会输出10个不同的值




