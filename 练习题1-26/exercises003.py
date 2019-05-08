#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 1.name = "aleX leNb "
'''
王振红day003
可直接运行
'''

name = "aleX leNb "
# 1.移除 name 变量对应的值两边的空格,并输出处理结果
new_name = name.strip()
print('-->', new_name, '<--')

# 2.判断 name 变量是否以 "al" 开头,并输出结果（用切片）
new_name1 = name[:2]
if new_name1[0] == 'a' and new_name1[1] == 'l':
    print('name是以al开头')
else:
    print('name不是以al开头')

# 3.判断name变量是否以"Nb"结尾,并输出结果（用切片）
if name[-1] == 'b' and name[-2] == 'N':
    print('name是以Nb结尾')
else:
    print('name不是以Nb结尾')

# 4.将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
print(name.replace('l', 'p'))


# 5.将name变量对应的值中的第一个"l"替换成"p",并输出结果
print(name.replace('l', 'p', 1))

# 6. 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
print(name.split('l'))

# 7.将name变量对应的值根据第一个"l"分割,并输出结果
print(name.split('l', 1))



# 8.将name变量对应的值变大写,并输出结果
print(name.upper())

# 9.将 name 变量对应的值变小写,并输出结果
print(name.lower())

# 10.请输出 name 变量对应的值的第 2 个字符?
print(name[1])

# 11.请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 12.请输出 name 变量对应的值的后 2 个字符?
print('-->', name[-2:], '<--')

# 2.有字符串s = "123a4b5c"
#    - 通过对s切片形成新的字符串 "123"
#    - 通过对s切片形成新的字符串 "a4b"
#    - 通过对s切片形成字符串s5,s5 = "c"
#    - 通过对s切片形成字符串s6,s6 = "ba2"
s = "123a4b5c"
print(s[:3])
print(s[3:6])
print(s[-1])
print(s[-3::-2])

# 3.使用while循环字符串 s="asdfer" 中每个元素。
s3 = "asdfer"
index3 = 0
while index3 < len(s3):
    print('3.遍历字符串: ', s3[index3])
    index3 += 1
else:
    index3 = 0

# 4.使用while循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
s4 = "321"
count4 = 0
while count4 < len(s4):
    print("倒计时%s秒" % (s4[count4]))
    count4 += 1
print('第4题', '出发!')

# 5.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9（含空白），然后进行分割转换最终进行整数的计算得到结果。
content = input("请输入* + *: ")
new_content = content.replace(" ", '')

count5 = 0
while 1:
    while count5 < len(new_content):
        if new_content[count5].isdigit():
            count5 += 1
            if new_content[count5].isdigit():
                continue
            new_content1 = int(new_content[:count5])
            break
            # if new_content[count5] == "+":
            #     pass
            # else:
            #     print('输入有误')
            # break
    if new_content[count5] == "+":
        pass
    else:
        print('输入有误')
        break

    index5 = len(new_content) - 1
    while index5 >= 0:
        if new_content[index5].isdigit():
            index5 -= 1
            if new_content[index5].isdigit():
                continue
            new_content2 = int(new_content[len(new_content)-index5:])
            break
    total = new_content1 + new_content2
    print(total)
    break

# 6.计算用户输入的内容中有几个 h 字符？
# 如：content = input("请输入内容：")
# 如fhdal234slfh98769fjdla
s6 = input('计算h的个数: ')
index6 = 0
count6 = 0
while index6 < len(s6):
    if s6[index6] == 'h':
        count6 += 1
    index6 += 1
print(count6)


# 7.计算用户输入的内容中有几个 h 或 H  字符？
# 如：content = input("请输入内容：")
# 如fhdal234slfH9H769fjdla
s7 = input('计算h和H的个数: ')
index7 = 0
count7 = 0
s71 = s7.lower()
while index7 < len(s7):
    if s71[index7] == 'h':
        count7 += 1
    index7 += 1
print(count7)


# 8.使用while循环分别正向和反向对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言。"。
message = "伤情最是晚凉天，憔悴厮人不堪言。"
index8 = 0
while index8 < len(message):
    print(message[index8])
    index8 += 1

index81 = len(message) - 1
while index81 >= 0:
    print(message[index81])
    index81 -= 1

# 9. 获取用户输入的内容中 前4个字符中 有几个 A ？
# 如：content = input("请输入内容：")   # 如fAdal234slfH9H769fjdla

content9 = input("请输入内容，判断前4个字符中有几个A：" )
index9 = 0
count9 = 0
while index9 < 4:
    if content9[index9] == 'A':
        count9 += 1
    index9 += 1
print(count9)

# 10.如果判断name变量对应的值前四位"l"出现几次,并输出结果。
index10 = 0
count10 = 0
name = input("前四位 l 出现几次： ")
while 1:
    if len(name) < 4:
        break
    while index10 < 4:
        if name[index10] == 'l':
            count10 += 1
        index10 += 1
    print('第10题', count10)
    break


# 11.获取用户两次输入的内容，并将所有的数据获取并进行相加
s11 = input('请输入内容1：')
s111 = input('请输入内容2：')
index11 = 0
s_1 = ''
while index11 < len(s11):
    if s11[index11].isdigit():
        s_1 += s11[index11]
    index11 += 1
    if s_1 == "":
        s_1 = 0

index111 = 0
s_2 = ''
while index111 < len(s111):
    if s111[index111].isdigit():
        s_2 += s111[index111]
    index111 += 1
    if s_2 == "":
        s_2 = 0
total = int(s_1) + int(s_2)
print(total)

