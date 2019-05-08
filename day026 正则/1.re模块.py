#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

"""
1. re.findall
"""
# ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
# print(ret) #结果 : ['a', 'a']

# w = re.findall('\btina', 'tian tinaaaa')
# print(w)
# s = re.findall(r'\bstina', 'tian tinaaaa')
# print(s)
# v = re.findall(r'\btina', 'tian#tinaaaa')
# print(v)
# a = re.findall(r'\btina\b', 'tian#tina@aaa')
# print(a)


# p = re.compile(r'\d+')
# print(p.findall('o11n22m333k4444'))

# import re
# tt = "Tina is a good girl, she is cool, clever, and so on..."
# rr = re.compile(r'\w*oo\w*')
# print(rr.findall(tt))
# print(re.findall(r'(\w)*oo(\w)', tt))  # ()表示子表达式


"""
2. re.compile
"""
# import re
# tt = "Tina is a good girl, she is coooool, clever, and so on..."
# rr = re.compile(r'\w*oo\w*')
# print(rr.findall(tt))   #查找所有包含'oo'的单词


"""
3. re.match
"""
# print(re.match('com', 'comwww.runcomoob').group())
# print(re.match('^com', 'aComwww.runcomoob'))
# print(re.match('^com', 'Comwww.runcomoob', re.I).group())


"""
4. re.search
"""
# print(re.search('\dcom', 'www.4comrunoob.5com').group())

# import re
# a = "123abc456"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))
# print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(4))


"""
5. re.finditer
"""
# iter = re.finditer(r'\d+', '12 drumm44ers drumming, 11 ... 10 ...')
# for i in iter:
#     print(i)
#     print(i.group())
#     print(i.span())

"""
6. re.split
"""
# print(re.split('\d+', 'one1two2three3four4five5  wwww', 2))


"""
7.re.sub
"""
# import re
# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# print(re.sub(r'\s+', '-', text, 2))

# import re
# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# print(re.sub(r'\s+', lambda m: '[' + m.group(0) + ']', text, 0))


"""
8. re.subn
"""
# print(re.subn('[1-2]', 'A', '123456abcdef'))
# print(re.sub("g.t", "have", 'I get A,  I got B ,I gut C'))
# print(re.subn("g.t", "have", 'I get A,  I got B ,I gut C'))


"""
search, match, findall 区别
"""
# a = re.search('[\d]', "abc34").group()
# print(a)
# p = re.match('[\d]', "abc44")
# print(p)
# b = re.findall('[\d]', "abc33")
# print(b)

