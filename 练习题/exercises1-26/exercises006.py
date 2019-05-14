#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  总结  ##################################
'''
1. 集合之间操作时，如果元素为空，则输出set()
2. 在循环里操作时，注意代码的有效范围
3. info.get('key', '不存在'）  # 可以返回两种不同的结果
4. 判断key是否在dict中只需：if key in info：
5. type(i) is int   # 这里的 int 是类
    tyep(i) == int  # 可以判断数据类型, 地址和内容都是一样

'''
############################   end   #################################



"""
1. 列举你了解的字典中的功能（字典独有）
"""
    # 1. info.keys()
    # 2. info.values()
    # 3. info.intems()
    # 4. info.pop('key')
    # 5. info.get('key', 666)
    # 6. info.update(info1)


"""
2. 列举你了解的集合中的功能（集合独有）。
"""
    # 1. v.add('a')
    # 2. v.discard('a')
    # 3. v.update(v2)  # v2 可以是list/tuple/set
    # 4. v = v1.intersectino(v2)
    # 5. v = v1.difference(v2)
    # 6. v = v1.union(v2)
    # 7. v = v1.sysmmetric_difference(v2)

"""
3. 列举你了解的可以转换为 布尔值且为False的值。
"""
    # None, 0, '', [], (), {}, set()

"""
4. 请用代码实现
   info = {'name':'王刚蛋','hobby':'铁锤'}
   - 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出。
   - 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出（如果key不存在，则获取默认“键不存在”，并输出）。
     注意：无需考虑循环终止（写死循环即可）
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤'}
#
# while True:
#     key = input('请输入key值：')
#     if key in info.keys():
#         message = info[key]
#     print(message)
#     message = "键不存在"

"""
5. 请用代码验证 "name" 是否在字典的键中？
   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# v = info.get('name', '不存在')
# print(v)


"""
6. 请用代码验证 "alex" 是否在字典的值中？
   info = {'name':'王刚蛋','hobby':'铁锤','age':'18',...100个键值对}
"""
# info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}
# message = "不存在"
# if 'alex' in info.values():
#     message = "存在"
# print(message)

"""
7. 有如下
   v1 = {'武沛齐','李杰','太白','景女神'}
   v2 = {'李杰','景女神}
   - 请得到 v1 和 v2 的交集并输出
   - 请得到 v1 和 v2 的并集并输出
   - 请得到 v1 和 v2 的 差集并输出
   - 请得到 v2 和 v1 的 差集并输出
"""
# v1 = {'武沛齐', '李杰', '太白', '景女神'}
# v2 = {'李杰', '景女神'}
# v = v1.intersection(v2)
# print(v)
# v = v1.union(v2)
# print(v)
# v = v1.difference(v2)
# print(v)
# v = v2.difference(v1)
# print(v)

"""
8. 循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
"""

# li = []
# while True:
#     content = input('请输入追加内容：')
#     if content.lower() == 'n':
#         break
#     li.append(content)
# print(li)

"""
9. 循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
"""
# u = set()
# while True:
#     content = input('请输入追加内容：')
#     if content.lower() == 'n':
#         break
#     u.add(content)
# print(u)


"""
10. 写代码实现
   v1 = {'alex','武sir','肖大'}
   v2 = []
   # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
"""
# v1 = {'alex', '武sir', '肖大'}
# v2 = []
# while True:
#     content = input('请输入追加内容：')
#     if content.lower() == 'n':
#         break
#     if content in v1:
#         v2.append(content)
#     else:
#         v1.add(content)
# print(v1, v2)



"""
11. 判断以下值那个能做字典的key ？那个能做集合的元素？
    - 1
    - -1
    - ""
    - None
    - [1,2]
    - (1,)
    - {11,22,33,4}
    - {'name':'wupeiq','age':18}
"""
li = [1, -1, "", None, [1, 2], (1,), {11, 22, 33, 4}, {'name': 'wupeiq', 'age': 18}]
new_li = []
for i in li:
    if type(i) is list or type(i) is dict or type(i) is set:
        pass
    else:
        new_li.append(i)
print("可以做字典的key或集合的元素有:")
for i in new_li:
    if i == "":
        print('""')
    else:
        print(i)


"""
12. is 和 == 的区别？
"""
    # == 是判断变量的值（内容）是否一致
    # is 是判断变量的内存地址是否一致

"""
13. type使用方式及作用？
"""
    # type()是查看变量的数据类型
    # eg. type(i)

"""
14. id的使用方式及作用？
"""
    # id() 查找i变量的内存地址
    # eg. id(i)

"""
15. 看代码写结果并解释原因
"""
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
# result1 = v1 == v2      # v1 与v2 内容一致，输出True
# result2 = v1 is v2      # 字典没有缓存机制，v1 v2 地址不同输出False
# print(result1)
# print(result2)


"""
16. 看代码写结果并解释原因
"""
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
#
# result1 = v1 == v2      # v1 v2，内容一致，输出True
# result2 = v1 is v2      # 由于赋值，v2中存储内容地址，与v1相同，输出True
# print(result1)
# print(result2)


"""
17. 看代码写结果并解释原因
"""
# v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2)       # v1是对'k1'的value值修改，v2内容也会随之更改

"""
18. 看代码写结果并解释原因
"""
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)       # v1是重新定义，会开辟新的地址空件，v2内容不会改变


"""
19. 看代码写结果并解释原因
"""
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
# info.append(9)
# print(userinfo)         # info进行追加，修改了内存空间中的值，userinfo中的也会同时改变
# info = "题怎么这么多"
# print(userinfo)         # info会开辟另一空间，usreinfo内容不会改变


"""
20. 看代码写结果并解释原因
"""
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)         # info内容发生改变，userinfo随之改变，所有info内容一样


"""
21. 看代码写结果并解释原因
"""
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
#
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)     # userinfo修改了内存中值，所有info都会改变


"""
22. 看代码写结果并解释原因
"""
# info = [1, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1] = "是谁说Python好学的？"
#
# print(user_list)    # info[1]修改了info 中的值，所有user_list中的info都会改变

"""
23. 看代码写结果并解释原因
"""
# data = {}
# for item in range(10):
#     data['user'] = item
# print(data)      # 由于字典中key值相同，最终只会输出一个值'user'：9

"""
24. 看代码写结果并解释原因
"""
# data_list = []
# data = {}
# for item in range(10):
#     data['user'] = item
#     data_list.append(data)
# print(data_list)    # 会输出10次一样的内容，{'user': 9}

"""
25. 看代码写结果并解释原因
"""
# data_list = []
# for item in range(10):
#     data = {}
#     data['user'] = item
#     data_list.append(data)
# print(data_list)     # 每次'user：item 都不同，因为date{}地址每循环一次，就会发生变化