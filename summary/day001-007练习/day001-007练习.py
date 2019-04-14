#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day001  ##################################01
"""
1. 操作系统的作用?
"""
    # 操作系统根据对应用程序请求使用计算机硬件资源的请求进行处理，
    # 为应用程序分配所需的硬件资源

"""
2. 列举你听过的操作系统及区别？
"""
    # windows(7, 8, 10, vista, server)
    # linux(centos, RedHat, ubuntu)
        # centos免费，主要用于中小企业
        # RedHat收费，主要用于大型企业
        # ubuntu开源，主要用于个人
    # macos(办公)


"""
3. 列举你了解的编码及他们之间的区别？
"""
    # ASCII，
        # 8bit编码，主要包含英文字母，及特殊字符，最多只能表示25个
    # unicode 万国码
        # 32bit编码，包含全球所有国家的文字，目前使用21bit
        # 浪费空间，远远超出目前所需
        # 主要用于计算机内部运算处理
    # utf-8
        # 对unicode进行压缩和优化，采用可变长度编码
        # 英文保留ASCII码，欧洲文字采用16bit，中文采用24bit
        # 编码长度是8的倍数
    # GB2312
        # 中文的编码，中文占用2byte
    # GBK
        # GB2312的扩展，也包含了亚洲其他国家的文字


"""
4. 列举你了解的Python2和Python3的区别？
"""
    # 解释器默认编码不同，py2 采用ASCII，py3采用utf-8
    # 输入输出格式不同
        # 输入：py2 raw_input(), py3:input()
        # 输出：py2 print "", py3: print()
    # int, long数据类型不同，py2 同时存在int和long，py3取消了long，扩展了int


"""
5. 你了解的python都有那些数据类型？
"""
    # None, int, bool, str, list, tuple, dict, set


"""
6. 补充代码，实现以下功能。
"""
# value = 'alex"烧饼'
# print(value)  # 要求输出  alex"烧饼


"""
7. 用print打印出下面内容：
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
"""
# s = """⽂能提笔安天下,
# 武能上⻢定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君
# """
# print(s)


"""
8. 变量名的命名规范和建议？
"""
# 1. 只能是数字、字母、下划线组成
# 2. 数字不能打头
# 3. 不能使用关键字
# 4. 推荐：见名知意， 驼峰式命名


"""
9. 如下那个变量名是正确的？
"""
# name = '武沛齐'   # 正确
# _ = 'alex'       # 正确
# _9 = "老男孩"     # 正确
# 9name = "景女神"  # 错误
# oldboy(edu = 666 # 错误


"""
10. 简述你了解if条件语句的基本结构。
"""
# 1.  if 条件判断：
#         代码
# 2.  if 条件判断：
#         代码
#     else：
# 3.  if 条件判断1：
#         代码1
#     elif 条件判断2:
#         代码2
#     elif 条件判断3:
#         代码3
#     ...
#     else:
#         代码4


"""
11. 设定一个理想数字比如：66，让用户输入数字，如果比66大，
    则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;
    只有等于66，显示猜测结果正确。
"""
# num = 66
# user_num = input('please input your num: ')
# if user_num.isdigit():
#     user_num = int(user_num)
#     if user_num > num:
#         print('猜大了')
#     elif user_num < num:
#         print('猜小了')
#     else:
#         print('猜对了')
# else:
#     print('输入有误')

"""
12. 提⽰⽤户输入⿇花藤. 判断⽤户输入的对不对。如果对, 提⽰真聪明, 如果不对, 提⽰你 是傻逼么。
"""
# user_s = input('please input ⿇花藤: ')
# if user_s == '⿇花藤':
#     print('真聪明')
# else:
#     print('你是傻逼么')

############################  day002  ##################################

"""
1. 猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；
    如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，然后退出循环。
"""
# num = 66
# while True:
#     user_num = input('please input your num: ')
#     if user_num.isdigit():
#         user_num = int(user_num)
#         if user_num > num:
#             print('猜大了')
#         elif user_num < num:
#             print('猜小了')
#         else:
#             print('猜对了')
#             break
#     else:
#         print('输入有误')


"""
2. 在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，
    如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’。
"""
# num = 66
# count = 0
# while True:
#     if count == 3:
#         break
#     user_num = input('please input your num: ')
#     count += 1
#     if user_num.isdigit():
#         user_num = int(user_num)
#         if user_num > num:
#             print('猜大了')
#         elif user_num < num:
#             print('猜小了')
#         else:
#             print('猜对了')
#             break
#     else:
#         print('输入有误')


"""
3. 使用两种方法实现输出 1 2 3 4 5 6   8 9 10 。
"""
# way1:
# for i in range(1, 11):
#     if i == 7:
#         continue
#     print(i)

# # way2:
# count = 1
# while count < 11:
#     if count != 7:
#         print(count)
#     count += 1


"""
4. 求1-100的所有数的和
"""
# total = 0
# for i in range(101):
#     total += i
# print(total)


"""
5. 输出 1-100 内的所有奇数
"""
# for i in range(1, 101, 2):
#     print(i)

"""
6. 输出 1-100 内的所有偶数
"""
# for i in range(2, 101, 2):
#     print(i)


"""
7. 求1-2+3-4+5 ... 99的所有数的和
"""
# total = 0
# for i in range(100):
#     if i % 2 == 1:
#         total += i
#     else:
#         total -= i
# print(total)

# way2
# total = 0
# for i in range(1, 100, 2):
#     total += i
# for i in range(2, 100, 2):
#     total -= i
# print(total)

"""
8. ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）
"""
# num = 66
# count = 3
# while count > 0:
#     s = '%s，您还剩余%s次机会'
#     user_num = input('please input your num: ')
#     count -= 1
#     if user_num.isdigit():
#         user_num = int(user_num)
#         if user_num > num:
#             print(s % ('猜大了', count,))
#         elif user_num < num:
#             print(s % ('猜小了', count,))
#         else:
#             print('猜对了')
#             break
#     else:
#         print(s % ('您的输入有误', count,))


"""
9. 简述ASCII、Unicode、utf-8编码
"""
# ASCII，
        # 8bit编码，主要包含英文字母，及特殊字符，最多只能表示25个
    # unicode 万国码
        # 32bit编码，包含全球所有国家的文字，目前使用21bit
        # 浪费空间，远远超出目前所需
        # 主要用于计算机内部运算处理
    # utf-8
        # 对unicode进行压缩和优化，采用可变长度编码
        # 英文保留ASCII码，欧洲文字采用16bit，中文采用24bit
        # 编码长度是8的倍数
    # GB2312
        # 中文的编码，中文占用2byte
    # GBK
        # GB2312的扩展，也包含了亚洲其他国家的文字


"""
10. 简述位和字节的关系？
"""
# 1 byte = 8 bit



"""
11. 猜年龄游戏 
    要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
"""
# age = 18
# count = 3
# while count > 0:
#     user_age = input('please input your age: ')
#     count -= 1
#     if user_age.isdigit():
#         user_age = int(user_age)
#         if user_age > age:
#             print('猜大了')
#         elif user_age < age:
#             print('猜小了')
#         else:
#             print('猜对了')
#             break
#     else:
#         print('您的输入有误')


"""
12. 猜年龄游戏升级版
    要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，
    就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。

"""
# age = 18
# count = 0
# while True:
#     if count == 3:
#         while True:
#             mean = input('是否继续，yes/no: ')
#             if mean == 'yes':
#                 count = 0
#                 break
#             elif mean == 'no':
#                 exit()
#             else:
#                 continue
#     user_age = input('please input your age: ')
#     count += 1
#     if user_age.isdigit():
#         user_age = int(user_age)
#         if user_age > age:
#             print('猜大了')
#         elif user_age < age:
#             print('猜小了')
#         else:
#             print('猜对了')
#             break
#     else:
#         print('您的输入有误')


"""
13. 判断下列逻辑语句的True,False
"""
# # True
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
#
# # Flase
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)



"""
14. 求出下列逻辑语句的值。
"""
# # 8
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
#
# # 4
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)

"""
15. 下列结果是什么？
"""
# print(6 or 2 > 1)   # 6
# print(3 or 2 > 1)   # 3
# print(0 or 5 < 4)   # Flase
# print(5 < 4 or 3)   # 3
# print(2 > 1 or 6)   # True
# print(3 and 2 > 1)  # True
# print(0 and 3 > 1)  # 0
# print(2 > 1 and 3)  # 3
# print(3 > 1 and 0)  # 0
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2) # 2


############################  day003  ##################################
"""
1. 有变量name = "aleX leNb " 完成如下操作： 
"""
name = "aleX leNb "
"""
移除 name 变量对应的值两边的空格,并输出处理结果
"""
# new_name = name.strip()
# print('-->', new_name, '<--')

"""
判断 name 变量是否以 "al" 开头,并输出结果（用切片）
"""
# s = 'name%s以"al"开头'
# if name[:2] == 'al':
#     print(s % ('是',))
# else:
#     print(s % ('不是',))

"""
判断name变量是否以"Nb"结尾,并输出结果（用切片）
"""
# s = 'name%s以"Nb"结尾'
# if name[-2:] == 'Nb':
#     print(s % ('是',))
# else:
#     print(s % ('不是',))
#


"""
将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果 
"""
# new_name = name.replace('l', 'p')
# print(new_name)


"""
将name变量对应的值中的第一个"l"替换成"p",并输出结果
"""
# new_name = name.replace('l', 'p', 1)
# print(new_name)


"""
将 name 变量对应的值根据 所有的"l" 分割,并输出结果
"""
# li = name.split('l')
# print(li)


"""
将name变量对应的值根据第一个"l"分割,并输出结果
"""
# li = name.split('l', 1)
# print(li)

"""
将 name 变量对应的值变大写,并输出结果
"""
# new_name = name.upper()
# print(new_name)

"""
将 name 变量对应的值变小写,并输出结果
"""
# new_name = name.lower()
# print(new_name)


"""
请输出 name 变量对应的值的第 2 个字符? 
"""
# print(name[1])


"""
请输出 name 变量对应的值的前 3 个字符? 
"""
# print(name[:3])

"""
请输出 name 变量对应的值的后 2 个字符?
"""
# print('-->', name[-2:], '<--')

"""
2. 有字符串s = "123a4b5c"
"""
"""
- 通过对s切片形成新的字符串 "123"
- 通过对s切片形成新的字符串 "a4b"
- 通过对s切片形成字符串s5,s5 = "c"
- 通过对s切片形成字符串s6,s6 = "ba2"
"""
# s = "123a4b5c"
# print(s[:3])
# print(s[3:6])
# print(s[-1])
# print(s[-3::-2])


"""
3. 使用while循环字符串 s="asdfer" 中每个元素。
"""
# s="asdfer"
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1

"""
4. 使用while循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
"""
# s = "321"
# count = 0
# flag = "倒计时%s秒"
# while count < len(s):
#     print(flag % s[count])
#     count += 1
# print('出发!')

"""
5. 实现一个整数加法计算器(两个数相加)：
如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9（含空白），
然后进行分割转换最终进行整数的计算得到结果。
"""
# content = input("请输入内容:")
# content = content.replace(' ', '')
# # print(int(content[0]) + int(content[-1]))
#
# li = content.split('+')
# print(int(li[0]) + int(li[-1]))

"""
6. 计算用户输入的内容中有几个 h 字符？
   如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
"""
# content = input("请输入内容：")
# new_content = content.replace('h', '')
# print(len(content) - len(new_content))

# count = 0
# for i in content:
#     if i == 'h':
#         count += 1
# print(count)


"""
7. 计算用户输入的内容中有几个 h 或 H  字符？
   如：content = input("请输入内容：")   # 如fhdal234slfH9H769fjdla
"""
# content = input("请输入内容：")
# content = content.lower()
# new_content = content.replace('h', '')
# print(len(content) - len(new_content))


# count = 0
# content = content.lower()
# for i in content:
#     if i == 'h':
#         count += 1
# print(count)



"""
8. 使用while循环分别正向和反向对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言。"。
"""
# message = "伤情最是晚凉天，憔悴厮人不堪言。"
# mes = ''
# mes2 = ''
# count = len(message) - 1
# while count >= 0:
#     mes += message[count]
#     mes2 += message[len(message) - 1 - count]
#     count -= 1
# print(mes)
# print(mes2)


"""
9. 获取用户输入的内容中 前4个字符中 有几个 A ？ 
   如：content = input("请输入内容：")   # 如fAdal234slfH9H769fjdla
"""
# content = input("请输入内容：")
# count = 0
# for i in content[:4]:
#     if i == 'A':
#         count += 1
# print(count)



"""
10. 如果判断name变量对应的值前四位"l"出现几次,并输出结果。
"""
# count = 0
# for i in name:
#     if i == 'l':
#         count += 1
# print(count)



"""
11. 获取用户两次输入的内容，并将所有的数据获取并进行相加，如：

要求：
    将num1中的的所有数字倒找并拼接起来：1232312
    将num1中的的所有数字倒找并拼接起来：1218323
    然后将两个数字进行相加。
"""
# num1 = input("请输入：") # asdfd123sf2312
# num2 = input("请输入：") # a12dfd183sf23
# num3 = ''
# num4 = ''
# for i in num1:
#     if i.isdigit():
#         num3 += i
#
# for i in num2:
#     if i.isdigit():
#         num4 += i
# print(int(num3) + int(num4))


############################  day004  ##################################

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


############################  day005  ##################################
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






############################  day006  ##################################


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
- 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出
（如果key不存在，则获取默认“键不存在”，并输出）。
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




############################  day007  ##################################
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
# info = []
# file_obj = open('data.txt', mode='r', encoding='utf-8')
# file = file_obj.read()
# file = file.strip('\n')
# file = file.split('\n')
#
# for i in file:
#     u, v, w = i.split('|')
#     line = {}
#     line['name'] = u
#     line['pwd'] = v
#     line['email'] = w
#     info.append(line)
# print(info)
# file_obj.close()