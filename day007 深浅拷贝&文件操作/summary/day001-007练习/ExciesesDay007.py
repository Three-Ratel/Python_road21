#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day007  ##################################
'''
1. file.readlines() 读出的是list类型
'''
#############################   end   ##################################


"""
1.看代码写结果
"""
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
#
# v1.append(6)
# print(v1)       # [1, 2, 3, 4, 5, 6]
# print(v2)       # [[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6]]


"""
2.看代码写结果
"""
# v1 = [1, 2, 3, 4, 5]
# v2 = [v1, v1, v1]
#
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)       # [222, 2, 3, 4, 5]
# print(v2)       # [[222, 2, 3, 4, 5], [222, 2, 3, 4, 5], [222, 2, 3, 4, 5]]




"""
3.看代码写结果，并解释每一步的流程。
"""
# v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# v2 = {}
#
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item]
# print(v2)  # {'k1': [6, 7 , 8, 9]}




"""
4.简述深浅拷贝？
"""
# 浅拷贝：只拷贝第一层可变类型的地址
# 深拷贝：拷贝所有可变类型的地址， tuple里嵌套可变类型是，tuple的地址也会copy
# 只要copy地址就会发生变化



"""
5.看代码写结果
"""
# import copy
#
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)  # True
# print(v1 is v3)  # True




"""
6.看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, 4, 5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1 is v2)     # Flase
# print(v1 is v3)     # Flase



"""
7.看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, 4, 5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])   # True
# print(v1[0] is v3[0])   # True
# print(v2[0] is v3[0])   # True




"""
8.看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, 4, 5]
#
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])   # True
# print(v1[0] is v3[0])   # True
# print(v2[0] is v3[0])   # True
#



"""
9.看代码写结果    
"""
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
#
# v2 = copy.copy(v1)
#
# print(v1 is v2)     # Flase
#
# print(v1[0] is v2[0])     # True
# print(v1[3] is v2[3])     # True
#
# print(v1[3]['name'] is v2[3]['name'])       # True
# print(v1[3]['numbers'] is v2[3]['numbers']) # True
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])   # True





"""
10.看代码写结果
"""
# import copy
#
# v1 = [1, 2, 3, {"name": '武沛齐', "numbers": [7, 77, 88]}, 4, 5]
#
# v2 = copy.deepcopy(v1)
#
# print(v1 is v2)       # Flase
#
# print(v1[0] is v2[0])   # True
# print(v1[3] is v2[3])   # Flase
#
# print(v1[3]['name'] is v2[3]['name'])             # True
# print(v1[3]['numbers'] is v2[3]['numbers'])       # False
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1]) # True



"""
11.简述文件操作的打开模式
"""
# 格式： open('filename', mode='r/w/a', encoding='utf-8')
# r：只读
# w：只写
# a：追加
#
# r+：读写，可以调整光标位置进行写入
# w+：写读，读取的时候必须调整光标位置
# a+：追加和读，只能在最后写入

"""
12.请将info中的值使用"_"拼接起来并写入到文件"readme.txt"文件中。
"""
# info = ['骗子，', '不是', '说', '只有', "10", '个题吗？']
# info = '_'.join(info)
# file_obj = open('readme.txt', mode='w', encoding='utf-8')
# file_obj.write(info)
# file_obj.close()




"""
13.请将info中的值使用"_"拼接起来并写入到文件"readme.txt"文件中。
"""
# info = ['骗子，', '不是', '说', '只有', 10, '个题吗？']
# info1 = []
# for i in info:
#     i = str(i)
#     info1.append(i)
# info1 = '_'.join(info1)
# file_obj = open('readme.txt', mode='w', encoding='utf-8')
# file_obj.write(info1)
# file_obj.close()




"""
14.请将info中的所有键使用"_"拼接起来并写入到文件"readme.txt"文件中。
# """
# 1. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# 2. 请将info中的所有值 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
# 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。


# info = {'name': '骗子', 'age': 18, 'gender': '性别'}
# info1 = []
# for i in info:
#     i = str(i)
#     info1.append(i)
# info1 = '_'.join(info1)
# file_obj = open('readme.txt', mode='w', encoding='utf-8')
# file_obj.write(info1)
# file_obj.close()
#
# info2 =[]
# for val in info.values():
#     val = str(val)
#     info2.append(val)
# info2 = '_'.join(info2)
# file_obj = open('readme.txt', mode='a', encoding='utf-8')
# file_obj.write('\n')
# file_obj.write(info2)
# file_obj.close()
#
#
# s1 = ''
# for i in info:
#     v = info[i]
#     s = '%s|%s,' % (i, v,)
#     s1 += s
# s = s1.strip(',')
# file_obj = open('readme.txt', mode='w', encoding='utf-8')
# file_obj.write(s)
# file_obj.close()


"""
15.写代码

要求：
如文件
data.txt
中有内容如下：

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
info = []
file_obj = open('data.txt', mode='r', encoding='utf-8')

file = file_obj.readlines()
for i in file:
    u, v, w = i.split('|')
    line = {}
    line['name'] = u
    line['pwd'] = v
    line['email'] = w
    info.append(line)
print(info)
file_obj.close()
