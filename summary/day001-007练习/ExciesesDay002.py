#!/usr/bin/env python
# -*- coding:utf-8 -*-

############################  day002  ##################################
'''
1. while True的效率会更高
2. 有时计数可以倒序
3. 一直要求用户输入，或者死循环需要使用while True
4. exit() 终止程序
'''
#############################   end   ##################################



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