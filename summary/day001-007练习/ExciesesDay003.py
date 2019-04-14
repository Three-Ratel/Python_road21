#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day003  ##################################
'''

'''
#############################   end   ##################################


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