#!/usr/bin/env python
# -*- coding:utf-8 -*-
############################  总结  ##################################
'''
1. 只要是'_'.join 处理过的，都是str
2. s.split('*') :
    默认是空白，实际应用中可以是字符或字符串
    循环去除
    但变量有且仅能是一个
'''
############################   end   #################################

"""
1.看代码写结果
"""
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v1.append(6)
# print(v1)     # [1, 2, 3, 4, 5, 6]
# print(v2)     # [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
#

"""
2. 看代码写结果
"""
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)       # [222, 2, 3, 4, 5]
# print(v2)       # [[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]

"""
3. 看代码写结果，并解释每一步的流程。
"""

# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)
# # {'k1': [6, 7, 8, 9]} ,item < 6 时continue之后的内容不会执行
# # item = 6 时， 由于v2 为空，所以会添加'k1': [6]
# # item = 7 时， 'k1'存在于v2中，v2['k1']表示列表[6],在列表中追加


"""
4. 简述深浅拷贝？
"""
    # 浅拷贝，只是拷贝可变类型的第一层地址，如果是不可变类型，则不开辟新的内存
    # 深拷贝，会拷贝所有可变类型的地址

"""
5. 看代码写结果
"""

# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)    # True
# print(v1 is v3)    # True

"""
6. 看代码写结果
"""

# import copy
# v1 = [1, 2, 3, 4, 5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)     # False
# print(v1 is v3)     # False


"""
7. 看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, 4, 5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])       # True
# print(v1[0] is v3[0])       # True
# print(v2[0] is v3[0])       # True


"""
8. 看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, 4, 5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])       # True
# print(v1[0] is v3[0])       # True
# print(v2[0] is v3[0])       # True


"""
9. 看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
# v2 = copy.copy(v1)
#
# print(v1 is v2)     # False
#
# print(v1[0] is v2[0])     # True
# print(v1[3] is v2[3])     # True
#
# print(v1[3]['name'] is v2[3]['name'])       # True
# print(v1[3]['numbers'] is v2[3]['numbers']) # True
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) # True

"""
10. 看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
#
# v2 = copy.deepcopy(v1)
#
# print(v1 is v2)       # Flase
#
# print(v1[0] is v2[0]) # True
# print(v1[3] is v2[3]) # False
#
# print(v1[3]['name'] is v2[3]['name'])               # True
# print(v1[3]['numbers'] is v2[3]['numbers'])         # False
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])   # True



"""
11. 简述文件操作的打开模式
"""
    # file_object = open('filename', mode='r/w/a', encoding='utf-8')
    # r：表示只读取文件内容
    # w：表示只写，文件存在先清空在写，不存在则创建
    # a：表示在文件内容最后追加，文件不存在则创建
    # r+：表示读写，默认在文件内容最后写，可以使用file_object.seek（n），移动光标位置，n表示字节数
    # w+：表示写读，在读取时，需要使用file_object.seek（n）移动光标位置
    # a+：表示追加和读取，但写只能在是追加

"""
12. 请将info中的值使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
"""
# info = ['骗子，', '不是', '说', '只有', "10", '个题吗？']
# info = '_'.join(info)
# file = open('readme.txt', mode='w', encoding='utf-8')
# file.write(info)
# file.close()


"""
13. 请将info中的值使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
"""
# info = ['骗子，', '不是', '说', '只有', "10", '个题吗？']
# info = '_'.join(info)
# file = open('readme.txt', mode='w', encoding='utf-8')
# file.write(info)
# file.close()


"""
14. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。

    info = {'name':'骗子','age':18,'gender':'性别'} 

    
    # 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。
"""
# # 1. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# k = []
# file = open('readme.txt', mode='w', encoding='utf-8')
# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# for key in info():
#     k.append(key)
# k = '_'.join(k)
# file.write(k)
# file.close()

# 2. 请将info中的所有值 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# v = []
# file = open('readme.txt', mode='w', encoding='utf-8')
# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# for val in info.values():
#     val = str(val)
#     v.append(val)
# v = '_'.join(v)
# file.write(v)
# file.close()

# # 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。
# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# v1 = ''
# file = open('readme.txt', mode='w', encoding='utf-8')
#
# for k in info:
#     v = "%s|%s," % (k, info[k],)
#     v1 += v
#     v2 = v1.strip(',')
# file.write(v2)
# file.close()

"""
15.
写代码
要求：如文件data.txt中有内容如下：
wupeiqi | oldboy | wupeiqi @ xx.com
alex | oldboy | 66
s @ xx.com
xxxx | oldboy | yuy @ xx.com
请用代码实现读入文件的内容，并构造成如下格式：
info = [
    {'name': 'wupeiqi', 'pwd': 'oldboy', 'email': 'wupeiqi@xx.com'},
    {'name': 'alex', 'pwd': 'oldboy', 'email': '66s@xx.com'},
    {'name': 'xxxx', 'pwd': 'oldboy', 'email': 'yuy@xx.com'},
]
"""
# info = []
# file = open('data.txt', mode='r', encoding='utf-8')
# line = file.read()
# line = line.strip('\n')
# line = line.split('\n')
#
# for i in line:
#     d = {}
#     u, v, w = i.split('|')
#     d['name'] = u
#     d['pwd'] = v
#     d['email'] = w
#     info.append(d)
# print(info)


