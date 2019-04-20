#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  总结  ##################################
'''
1. 当使用s.isdigit()时要注意，s 的数据类型
2. list(dic.keys()) # 可以强转为list，如果是items则list元素为tuple
'''
############################   end   #################################


"""
1. 请将列表中的每个元素通过 "_" 链接起来。
"""
# users = ['李少奇', '李启航', '渣渣辉']
# users = '_'.join(users)
# print(users)

"""
2. 请将列表中的每个元素通过 "_" 链接起来。
"""
# users = ['李少奇', '李启航', 666, '渣渣辉']
# u = str(users)
# users = u.split(',')
# users = '_'.join(users)
# print(users)

"""
3. 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。 
"""
# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# v2.extend(v1)
# print(v2)

"""
4. 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
"""
# v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# v2 = [44, 55, 66]
# v3 = []
# for i in range(0, len(v1), 2):
#     v3.append(v1[i])
# v2.extend(v3)
# print(v2)

"""
5. 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
"""
# key_list = []
# value_list = []
# info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
#
# for u, v in info.items():
#     key_list.append(u)
#     value_list.append(v)
# print(key_list)
# print(value_list)


"""
6. 字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
    a. 请循环输出所有的key
    b. 请循环输出所有的value
    c. 请循环输出所有的key和value
    d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
    e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
    f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
    g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
"""
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# for u in dic.keys():
#     print(u)
# for v in dic.values():
#     print(v)
# for u, v in dic.items():
#     print(u, v)
#
# dic['k4'] = 'v4'
# print(dic)
#
# dic['k1'] = 'alex'
# print(dic)
#
# dic['k3'].append(44)
# print(dic)
#
# dic['k3'].insert(0, 18)
# print(dic)

"""
7. 请循环打印k2对应的值中的每个元素。
   info = {
       'k1':'v1',
       'k2':[('alex'),('wupeiqi'),('oldboy')],
   }
"""
# info = {
#     'k1': 'v1',
#     'k2': [('alex'), ('wupeiqi'), ('oldboy')],
# }
# for item in info['k2']:
#     for i in item:
#         print(i)


"""
8. 有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....} 
"""
# dic = {}
# s = 'k: 1|k1:2|k2:3  |k3 :4'
# li = s.split('|')
# for item in li:
#     u, v = item.split(':')
#     u1 = u.strip()
#     v1 = v.strip()
#     dic[u1] = v1
# print(dic)

"""
9. 写代码
   有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保
   存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
   result = {'k1':[],'k2':[]}
"""
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# result = {'k1': [], 'k2': []}
# for i in li:
#     if i > 66:
#         result['k1'].append(i)
#     elif i < 66:
#         result['k2'].append(i)
#     else:
#         pass
# print(result)


"""
10. 输出商品列表，用户输入序号，显示用户选中的商品
   商品列表：
     goods = [
   		{"name": "电脑", "price": 1999},
   		{"name": "鼠标", "price": 10},
   		{"name": "游艇", "price": 20},
   		{"name": "美女", "price": 998}]
   要求:
   1：页面显示 序号 + 商品名称 + 商品价格，如：
         1 电脑 1999 
         2 鼠标 10
   2：用户输入选择的商品序号，然后打印商品名称及商品价格
   3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
   4：用户输入Q或者q，退出程序。
"""
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}
# ]
# count = 1
# for i in goods:
#     print(count, i['name'], i['price'])
#     count += 1
#
# while True:
#     num = input('输入序号：')
#     if num.isdigit() and 0 < int(num) < 5:
#         num1 = int(num)
#         u = goods[num1 - 1]['name']
#         v = goods[num1 - 1]['price']
#         print(u, v)
#         break
#     elif num.upper() == 'Q':
#         print('已退出')
#         break
#     else:
#         print('输入有误，请重新输入')


"""
11. 看代码写结果
"""
# v = {}
# for index in range(10):
#     v['users'] = index
# print(v)
# # 只有一个值为{'users',9}