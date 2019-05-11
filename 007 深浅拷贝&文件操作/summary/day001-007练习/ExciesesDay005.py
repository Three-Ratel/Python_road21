#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day005  ##################################
'''
1. users = '_'.join(users) 此操作一定要使用新的变量接受
    因为通过 join 处理过的数据都会变成str类型
2. dict的items 输出是tuple 类型
'''
#############################   end   ##################################
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
# new_users = []
# for i in users:
#     new_users.append(str(i))
# new_users = '_'.join(new_users)
# print(new_users)


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
# v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# v3 = v1[::2]
# v2.extend(v3)
# print(v2)

"""
5. 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
"""
# key_list = []
# value_list = []
# info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# for i in info:
#     key_list.append(i)
# for v in info.values():
#     value_list.append(v)
# print(key_list, value_list)


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
# for key in dic:
#     print(key)
# for value in dic.values():
#     print(value)
# for item in dic.items():
#     print(item)
# dic['k4'] = 'v4'
# print(dic)
#
# dic['k1'] = 44
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
#        'k1': 'v1',
#        'k2': [('alex'),('wupeiqi'),('oldboy')],
#    }
# for i in info['k2']:
#     print(i)


"""
8. 有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....} 
"""
# info = {}
# s = 'k: 1|k1:2|k2:3  |k3 :4'
# li = s.split('|')
# for i in li:
#     u, v = i.split(':')
#     if v.isdigit():
#         v = int(v)
#     info[u] = v
# print(info)


"""
9. 写代码
   有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 
   的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key
   对应的列表中。
   result = {'k1':[],'k2':[]}
"""
# result = {'k1': [], 'k2': []}
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90, 'hello']
# for i in li:
#     if type(i) == int:
#         if i > 66:
#             result['k1'].append(i)
#         elif i < 66:
#             result['k2'].append(i)
#         else:
#             pass
# print(result)



"""
10. 输出商品列表，用户输入序号，显示用户选中的商品
   商品列表：
     goods = [
   		{"name": "电脑", "price": 1999},
   		{"name": "鼠标", "price": 10},
   		{"name": "游艇", "price": 20},
   		{"name": "美女", "price": 998}
   	]
   要求:
   1：页面显示 序号 + 商品名称 + 商品价格，如：
         1 电脑 1999 
         2 鼠标 10
   	  ...
   2：用户输入选择的商品序号，然后打印商品名称及商品价格
   3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
   4：用户输入Q或者q，退出程序。
"""
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}
#     ]
# count = 1
# for i in goods:
#     print(count, i['name'], i['price'])
#     count += 1
# while True:
#     num = input('please input your num(Q/q 退出): ')
#     if num.upper() == 'Q':
#         break
#     if num.isdigit() and 0 < int(num) < 5:
#         num = int(num)
#         print('%s  %s' % (goods[num - 1]['name'], goods[num - 1]['price']))
#     else:
#         print('your num is wrong')



"""
11. 看代码写结果
"""
# v = {}
# for index in range(10):
#     v['users'] = index
# print(v)      # v = {'users': 9}






