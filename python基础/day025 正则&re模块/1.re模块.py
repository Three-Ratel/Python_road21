#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

"""
1.re.findall
"""
# ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
# print(ret) #结果 : ['a', 'a']


"""
2.re.search
"""
# ret = re.search('a', 'eva egon yuan').group()
# print(ret) #结果 : 'a'
# # 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。


"""
3.re.match
"""
# ret = re.match('a', 'abc')  # 同search,不过尽在字符串开始处进行匹配
# print(ret.group())     # 结果 : 'a'


"""
4.re.split
"""
ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']


"""
5. re.sub
"""
# ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
# print(ret) #evaHegon4yuan4
#
# ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
# print(ret)
#
# obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
# ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
# print(ret.group())  #结果 ： 123
#

# ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
# print(ret)  # <callable_iterator object at 0x10195f940>
# print(next(ret).group())  #查看第一个结果
# print(next(ret).group())  #查看第二个结果
# print([i.group() for i in ret])  #查看剩余的左右结果




