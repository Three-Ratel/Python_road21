#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则表达式练习
# 1、匹配一篇英文文章的标题 类似 The Voice Of China
# import re
# ret = re.findall(r'(?:[A-Z](?:[a-zA-z]+)?\s?)+', 'The Voice Of China')
# print(ret)


# 2、匹配一个网址
# s = 'https://www.baidu.com http://www.cnblogs.com'
# ret = re.findall('https?://www\.\w+\.com', s)
# print(ret)


# 3、匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# s = '2018-12-06 2018/12/06 2018.12.06'
# ret = re.findall('\d{4}.?\d{2}.?\d{2}', s)
# print(ret)

# 4、匹配15位或者18位身份证号
# s = '34121219990101123434121219990101123x341212199901011'
# ret = re.findall(r'\d{17}[\dXx]|\d{15}', s)
# print(ret)


# 5、从lianjia.html中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', \
# '2室1厅', '94.14平米')]
# import re
# import json
# import requests
# data = requests.get('https://bj.lianjia.com/ershoufang/')
# content = data.text
# f = open('lj.html', mode='w',encoding='utf-8')
# json.dump(content, f)
# f.close()


f = open('lianjia.html', mode='r', encoding='utf-8')
content = f.read()
f.close()
import re
ret = re.findall('<div class="title">.*?>(.*?)<.*?"houseInfo">.*?/span>(.*?)<.*?/span>(.*?)<.*?/div>',
                 content, flags=re.S)

print(ret)

# 6、
# s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
# import re
# # ret = re.findall('-?\d+[*/\-+]\d+(?:(?:[*/+-]\d+)+)?', s)
# ret = re.findall('-?\d+[*/\-+]\d+(?:[*/+-]\d+)*', s)
# print(ret)


# 7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法
# import re
# ret = re.findall('\d+[*/]\d+(?:[*/]\d+){0,}', '9-2*5/3+7/3*99/4*2998+10*568/14')
# print(ret)


# 8、通读博客，完成三级菜单
# http://www.cnblogs.com/Eva-J/articles/7205734.html


# 9、大作业：计算器
"""
1)如何匹配最内层括号内的表达式
2)如何匹配乘除法
3)考虑整数和小数
4)写函数，计算‘23’ ‘10/5’
5)引用4)中写好的函数，完成'23/4'计算
"""
# import re
# li = []
# s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# # ret = re.findall(r'(?<=\()-?\d+[*/+-]\d+(?:[*/+-]\d+)*(?=\))', s)
# ret = re.findall(r'(?<=\()[*/+\-\d\.]+(?=\))', s)
# # print(ret)
#
#
# i = '40/5'
# def exp(i):
#     for j in range(1, len(i)):
#         if i[j].isdecimal():
#             continue
#         break
#     v = re.split((i[j]), i)
#     v.append(i[j])
#     return v
#
#
# li = exp(i)
# print(li)
# res = 1
# for i in li:
#     k = li[-1]
#     res k= int(i)
# print(res)
