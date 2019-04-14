# 猜大小
# num = 66
# while True:
#     user_num = int(input('please enter your num: '))
#     if user_num > 66:
#         print('猜大了')
#     elif user_num < 66:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break


# 猜大小升级版
# num = 66
# count = 1
# while count <= 3:
#     user_num = int(input('please enter your num: '))
#     if user_num > 66:
#         print('猜大了', '\n', '你还有%s次机会' % (3-count))
#     elif user_num < 66:
#         print('猜小了', '\n', '你还有%s次机会' % (3-count))
#     else:
#         print('猜对了')
#         break
#     count += 1
# else:
#     print('大笨蛋')


# 输出1，2，3，4，5，6，8，9，10
# count = 1
# while count <= 10:
#     if count != 7:
#         print(count)
#     count += 1

# count = 0
# while True:
#     count += 1
#     if count == 7:
#         continue
#     if count > 10:
#         break
#     print(count)


# count = 1
# while count <= 10:
#     if count == 7:
#         count += 1
#         continue
#     print(count)
#     count += 1

# 100以内总和
# count = 1
# total = 0
# while count <= 100:
#     total += count
#     count += 1
# print(total)

# 100以内所有奇数
# count = 1
# while count <= 100:
#     if count % 2 == 1:
#         print(count)
#     count += 1


# 100以内所有偶数
# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count += 1


# 1-2+3-4...+99
# count = 1
# total = 0
# while count < 100:
#     if count % 2 == 1:
#         total += count
#     else:
#         total -= count
#     count += 1
# print(total)


# 用户登陆，共3次机会
# count = 1
# name = 'henry'
# password = str(123)
#
# while count <= 3:
#     user_name = input('请输入用户名: ')
#     pwd = input('请输入密码：')
#     if user_name == name and pwd == password:
#         print('恭喜你，登陆成功')
#         break
#     else:
#         print('用户名或密码错误', '\n', '你还有%s次机会' % (3 - count))
#     count += 1


# 猜年龄游戏
# count = 1
# age = 18
#
# while count <= 3:
#     user_age = input('请输入年龄: ')
#     if user_age == age:
#         print('恭喜你，猜对了')
#         break
#     else:
#         print('猜错了', '\n', '你还有%s次机会' % (3 - count))
#     count += 1

# 猜年龄游戏升级版
# 第一种方法
# count = 1
# age = 18
#
# while True:
#     while count <= 3:
#         user_age = input('请输入年龄: ')
#         if user_age == age:
#             print('恭喜你，猜对了')
#             break
#
#         print('猜错了', '\n', '你还有%s次机会' % (3 - count))
#         count += 1
#     else:
#         user = input('是否继续：继续请输入Y，退出请输入N:')
#         if user == 'Y':
#             count = 1
#             continue
#         elif user == 'N':
#             break
#         else:
#             continue
#
#     break


# 第二种方法
count = 1
age = 18
while True:
    user_age = input('请输入年龄: ')
    if user_age.isdigit():
        print('输入有误，请重新输入')
        continue

        user_age = int(user_age)

        if user_age == age:
            print('恭喜你，猜对了')
            break
        print('猜错了', '\n', '你还有%s次机会' % (3 - count))
        count += 1
        if count == 4:
            user = input('是否继续：继续请输入Y，退出请输入N:')
            if user == 'Y':
                count = 1
            elif user == 'N':
                break
            else:
                print('输入有误')
                count = 1

# print(8 or 3 and 4 or 2 and 0 or 9 and 7)




