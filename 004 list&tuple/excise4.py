#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
day004 王振红
'''


"""
1.简述解释性语言和编译型语言的区别？
 解释型语言：代码 --> 解释器 --> 计算机计算
    例如：python, ruby, php
 编译型语言：代码 --> 编译器 --> .h(或其他格式文件) --> 计算机计算
    例如：C, C++, C# , Java, Go
"""

"""
2.列举你了解的Python的数据类型？
    int
    bool
    str
    list
    tuple
"""

"""
# 3.写代码，有如下列表，按照要求实现每一个功能。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

# 计算列表的长度并输出
print(len(li))

# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(li[::2])

# 列表中追加元素"seven",并输出添加后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.append("seven")
print(li)

# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.insert(0, "Tony")
print(li)

# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li[1] = 'Kelly'
print(li)

# 请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li[2] = '太白'
print(li)

# 请将列表 l2=[1,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2 = [1, "a", 3, 4, "heart"]
for i in range(0, len(l2)):
    li.append(l2[i])
print(li)

# 请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
s = "qwert"
li.extend(s)
print(li)

# 请删除列表中的元素"ritian",并输出添加后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.remove('ritian')
print(li)

# 请删除列表中的第2个元素，并输出删除元素后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li.pop(1)
print(li)

# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li2 = []
count = len(li)
for i in range(0, count):
    if 2 <= i <=4:
        continue
    li2.append(li[i])
print(li2)
"""

"""
# 请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for)
# 方法一
name = "小黑半夜三点在被窝玩愤怒的小鸟"
name1 = name[::-1]
print(name1)

#方法二
name = "小黑半夜三点在被窝玩愤怒的小鸟"
count = len(name) - 1
name1 = ''
while 1:
    name1 += name[count]
    count -= 1
    if count == -1:
        break
print(name1)

# 方法三
name = "小黑半夜三点在被窝玩愤怒的小鸟"
count = 0
name2 = ''
for i in range(len(name)):
    name2 += name[len(name) - 1 - i]
print(name2)
"""

"""
#5.写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# - 通过对li列表的切片形成新的列表 [1,3,2]
print(li[:3])
# - 通过对li列表的切片形成新的列表 ["a",4,"b"]
print(li[3:6])
# - 通过对li列表的切片形成新的列表  [1,2,4,5]
print(li[::2])
# - 通过对li列表的切片形成新的列表 [3,"a","b"]
print(li[1:7:2])
# - 通过对li列表的切片形成新的列表 [3,"a","b","c"]
print(li[1::2])
# - 通过对li列表的切片形成新的列表  ["c"]
print(li[-1])
# - 通过对li列表的切片形成新的列表 ["b","a",3]
print(li[-3:0:-2])
"""
"""
# 6.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# 0 武沛齐
# 1 景女神
# 2 肖大侠
users = ["武沛齐", "景女神", "肖大侠"]
for i in range(0, len(users)):
    print(i, users[i])
"""
"""
# 8. 写代码，有如下列表，按照要求实现每一个功能。
# 将列表lis中的"k"变成大写，并打印列表。
# 将列表中的数字3变成字符串"100"
# 将列表中的字符串"tt"变成数字 101
# 在 "qwe"前面插入字符串："火车头"
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[2] = 'K'
print(lis)
lis[1] = '100'
lis[3][2][1][1] = '100'
print(lis)
lis[3][2][1][0] = 101
print(lis)
lis.insert([3][0], '火车头')
print(lis)
"""

"""
# 9. 写代码实现以下功能
#
# 如有变量 googs = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
#
#      0,汽车
#      1,飞机
#      2,火箭
#
# 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
googs = ['汽车', '飞机', '火箭']
for i in range(0, len(googs)):
    print(i, googs[i])

num = int(input('请选择序号：'))
if 0 <= num < 3:
    print('您选择的商品是%s' %(googs[num],))
else:
    print("您的输入有误")
"""
"""
# 10.请用代码实现
# li = "alex"
# 利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
li = "alex"
li = '_'.join(li)
print(li)
"""

"""
# 11.利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
li = []
for i in range(0, 100):
    if i % 2 == 0:
        li.append(i)
print(li)
"""

"""
# 12.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
li = []
for i in range(0, 50):
    if i % 3 == 0:
        li.append(i)
print(li)
"""

"""
# 13. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
#    [48,45,42...]
li = []
for i in range(0, 50):
    if i % 3 == 0:
        li.insert(0, i)
print(li)
"""

"""
# 14. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
new_li = []
for i in range(0, len(li)):
    s = li[i]
    s1 = s.strip()
    if s1.startswith('a'):
        new_li.append(s1)
print(new_li)
"""

"""
# 15.判断是否可以实现，如果可以请写代码实现。
# li = ["alex",[11,22,(88,99,100,),33] "WuSir", ("ritian", "barry",), "wenzhou"]
# 请将 "WuSir" 修改成 "武沛齐"
# 请将 ("ritian", "barry",) 修改为 ['日天','日地']
# 请将 88 修改为 87
# 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry"), "wenzhou"]
li[2] = "武沛齐"
print(li)

li[-2] = ['日天', '日地']
print(li)

li[1][2] = (87, 99, 100)
print(li)

li.pop()
li.insert(0, "文周")
print(li)
"""

