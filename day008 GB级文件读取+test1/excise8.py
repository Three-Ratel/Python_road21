#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
19. 读取100G文件, 文件在本目录，文件名为test.txt, 写入文件名为new_test.txt
"""

# keys = ['苍老师', '小泽老师', 'alex']
# with open('a.txt', mode='r', encoding='utf-8') as v1,  \
# open('new_test.txt', mode='w', encoding='utf-8') as v2:
#     for i in v1.readlines():
#         for key in keys:
#             if key in i:
#                 i = i.replace(key, '***')

        # i = i.replace('苍老师', '***')
        # i = i.replace('小泽老师', '***')
        # i = i.replace('alex', '***')
        # v2.write(i)
# keys = ['苍老师', '小泽老师', 'alex']
# with open('a.txt', mode='r', encoding='utf-8') as f1,  \
# open('new_test.txt', mode='w', encoding='utf-8') as f2:
#     for line in f1:
#         for key in keys:
#             line = line.replace(key, '***')
#         f2.write(line)


"""
20. 计算车牌归属数量
"""
# cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
# info = {}
# li = []
# u = set()
# for i in cars:
#     li.append(i[0])
#
# for i in set(li):
#     count = li.count(i)
#     info[i] = count
# print(info)

"""
way2
"""
# info = {}
# for item in cars:
#     start = item[0]
#     if start in info:
#         info[start] = info[start] + 1
#     else:
#         info[start] = 1


"""
21. 读取文件内容
"""
# info = []
# li = []
#
# with open('data.txt', mode='r', encoding='utf-8') as v:
#     file_obj = v.read()
#     file_obj = file_obj.split('\n')
#     print(file_obj)
#     for i in file_obj:
#         li.append(i)
# li1 = li[0].split(',')
# li2 = li[1:]
# for i in li2:
#     msg = {}
#     u, v, w, x, y = i.split(',')
#     msg[li1[0]] = u
#     msg[li1[1]] = v
#     msg[li1[2]] = w
#     msg[li1[3]] = x
#     msg[li1[4]] = y
#     info.append(msg)
# print(info)


"""
way2
"""
# info = []
# with open('data.txt', mode='r', encoding='utf-8') as v:
#     li = v.read().split('\n')
#
# li1 = li[0].split(',')
# li2 = li[1:]
#
# for i in li2:
#     l = i.split(',')
#     mes = {}
#     for j in range(len(li1)):
#         mes[li1[j]] = l[j]
#         info.append(mes)
# print(info)



"""
way3 
"""
info = []
with open('data.txt', mode='r', encoding='utf-8') as f:
    is_first = True
    first_line_list = None
    for line in f:
        line = line.strip()
        if is_first:
            first_line_list = line.split(',')
            is_first = False
            continue
        other_line_list = line.split(',')
        element = {}
        for i in range(0, len(other_line_list)):
            element[first_line_list[i]] = other_line_list[i]
        info.append(element)
print(info)


"""
22.for 循环打印9*9乘法表
"""

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%s*%s ' % (i , j), end='')
#         if i == j:
#             print("")


