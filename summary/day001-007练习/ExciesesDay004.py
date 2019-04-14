#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day004  ##################################
'''
1.
'''
#############################   end   ##################################


"""
1. 简述解释性语言和编译型语言的区别？
"""
# 解释性语言是通过解释器，逐条解释代码并执行
# 编译型语言是先编译整个代码文件，生成能被计算机识别的二进制文件，在交给计算机执行


"""
2. 列举你了解的Python的数据类型？ 
"""
# None, int, bool, str, list, dict, set


"""
3. 写代码，有如下列表，按照要求实现每一个功能。
- 计算列表的长度并输出
- 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
- 列表中追加元素"seven",并输出添加后的列表
- 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
- 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
- 请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
- 请将列表 l2=[1,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
- 请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
- 请删除列表中的元素"ritian",并输出添加后的列表
- 请删除列表中的第2个元素，并输出删除元素后的列表
- 请删除列表中的第2至第4个元素，并输出删除元素后的列表
"""
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))
#
# print(li[::2])
#
# li.append('seven')
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.insert(0, 'Tony')
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li[1] = 'Kelly'
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li[2] = '太白'
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# l2 = [1, "a", 3, 4, "heart"]
# li.extend(l2)
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# s = "qwert"
# li.extend(s)
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.remove('ritian')
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li.pop(2)
# print(li)
#
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# del li[1:4]
# print(li)

"""
4. 请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for）
"""
# name = "小黑半夜三点在被窝玩愤怒的小鸟"
# print(name[::-1])
#
# count = len(name) - 1
# name1 = ''
# while count >= 0:
#     name1 += name[count]
#     count -= 1
# print(name1)
#
# name2 = ''
# count = 0
# for i in range(len(name)):
#     name2 += name[len(name) -1 - count]
#     count += 1
# print(name2)


"""
5. 写代码，有如下列表，利用切片实现每一个功能
   - 通过对li列表的切片形成新的列表 [1,3,2]
   - 通过对li列表的切片形成新的列表 ["a",4,"b"] 
   - 通过对li列表的切片形成新的列表  [1,2,4,5]
   - 通过对li列表的切片形成新的列表 [3,"a","b"]
   - 通过对li列表的切片形成新的列表 [3,"a","b","c"]
   - 通过对li列表的切片形成新的列表  ["c"]
   - 通过对li列表的切片形成新的列表 ["b","a",3]
"""
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# print(li[:3])
# print(li[3:6])
# print(li[::2])
# print(li[1:-2:2])
# print(li[1::2])
# print(li[-1])
# print(li[-3:0:-2])


"""
6. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
   0 武沛齐
   1 景女神
   2 肖大侠
"""
# users = ["武沛齐", "景女神", "肖大侠"]
# for i in range(len(users)):
#     print(i, users[i])


"""
7. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
   1 武沛齐
   2 景女神
   3 肖大侠
"""
# 同第6题


"""
8. 写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
   - 将列表lis中的"k"变成大写，并打印列表。
   - 将列表中的数字3变成字符串"100"
   - 将列表中的字符串"tt"变成数字 101
   - 在 "qwe"前面插入字符串："火车头"
"""
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# for i in range(len(lis)):
#     if lis[i] == 'k':
#         lis[i] = 'K'
# print(lis)

"""
9. 写代码实现以下功能
- 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
     0,汽车
     1,飞机
     2,火箭
- 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
"""
# goods = ['汽车', '飞机', '火箭']
# for i in range(len(goods)):
#     print(i, goods[i])
# num = input('please input your num: ')
# if num.isdigit() and 0 <= int(num) < 3:
#     num = int(num)
#     print('your choice is: %s' % goods[num])
# else:
#     print('your input is worng')


"""
10. 请用代码实现  
    li = "alex"
    利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
"""
# li = "alex"
# li = '_'.join(li)
# print(li)

# li = "alex"
# s = ''
# for i in li:
#     s += '%s_' % i
# s = s.strip('_')
# print(s)



"""
11. 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
"""
# li = []
# for i in range(0, 100, 2):
#     li.append(i)
# print(li)

"""
12. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
"""
# li = []
# for i in range(0, 50, 3):
#     li.append(i)
# print(li)


"""
13. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
    [48,45,42...]
"""
# li = []
# for i in range(0, 50, 3):
#     li.insert(0, i)
# print(li)

"""
14. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
"""
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# l1 = []
# for i in li:
#     i = i.strip()
#     if i.startswith('a'):
#         l1.append(i)
# for i in l1:
#     print(i)


"""
15. 判断是否可以实现，如果可以请写代码实现
    - 请将 "WuSir" 修改成 "武沛齐"
    - 请将 ("ritian", "barry",) 修改为 ['日天','日地']
    - 请将 88 修改为 87 
    - 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
"""
# li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
# for i in range(len(li)):
#     if li[i] == 'WuSir':
#         li[i] = '武沛齐'
# print(li)
#
# for i in range(len(li)):
#     if li[i] == ("ritian", "barry",):
#         li[i] = ['日天', '日地']
# print(li)
#
#
# li[1][2] = (87, 99, 100)
# print(li)
#
# li.pop()
# li.insert(0, "文周")
# print(li)