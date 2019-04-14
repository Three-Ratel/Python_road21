# 练习题 % 求余数
# count = 1
# sum = 0
# while True:
#     sum += count
#     count += 1
#     if count > 100:
#         break
# print(sum)


# 打印100以内的奇数
# count = 1
# while count <= 100:
#     if count % 2 == 1:
#         print(count)
#     count += 1

# if 1 > 0 and 1 < 2:
#     print('666')

# ** 幂次方
# // 地板除


# 练习1-100数之和

# count = 1
# sum = 0
# while count <= 100:
#     sum += count
#     count += 1
# print(sum)


# str转bool
# int转bool
# str转int（前提：可转）
# int转str

# Note：
# or 如果时 value = 0 or 9，如果第一值为真，则采用。否则，value = 第二个值
# 如果有多个or，从左到右依次进行计算
# 第一个不为0的，或者取最后一个

# value = 1 or 9
# print(value)
#
# value = 0 or 9
# print(value)
#
# value = 0 or ''
# print('-->',value,'<--')

# 如果第一个值是True，取决于第二个值，否则，第一个值
# 多个and条件，依次计算
# 第一个为0的，或者最后一个

# 优先级:not -> and -> or

v1 = 1 and 9 or 0 and 6
print(v1)