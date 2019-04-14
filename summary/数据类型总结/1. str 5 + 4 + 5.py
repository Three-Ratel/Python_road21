#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
str的操作： 目前有15（5 + 5 + 5）种
"""
# # 1. str大小写转换
# s = 'Henry'
# print(s.upper(), s.lower())


# # 2. s.isdigit()
# s1 = '123'
# s2 = '12.3'
# print(s1.isdigit(), s2.isdigit())


# # 3. s.strip()
# s = '  asdfgh,        '
# print('-->', s.strip(), '<--')
# print('-->', s.strip().strip(','), '<--')

# # 4. s.replace('a', 'b', 2)
# s = 'adsafga'
# print(s.replace('a', '666'))
# print(s.replace('a', '666', 1))

# # 5. s.split('_')
# s = 'henry_echo_elaine_'
# li = s.split('_')
# print(li)

# # 6. s.startswith('ab') / s.endswith('cd')
# s = 'abghjkdc'
# print(s.startswith('ab'), s.endswith('cd'))


# # 7.str 的格式化输出(2种)
# # way1 '{0} ***{1}'.format(a, b)
# a = 'abcd'
# b = '666'
# s = '{0}***{1}'.format(a, b)
# print(s)
# # way2
# s1 = '%s***%s' % (a, b,)
# print(s1)

# # 8. encode
# s = '你好'
# print(s.encode('utf-8'))   # 6个字节
# print(s.encode('gbk'))	   # 4个字节

# # 9.'_'.join(s)
# s = 'henry'
# print('_'.join(s))

# # 10. len(s)
# s = '1234567890'
# print(len(s))

# # 11. s[index]
# s = '123456789'
# print(s[3])   # 4


# # 12. 切片
# s = '123456789'
# print(s[3:5])   # 4


# # 13. step
# s = '123456789'
# print(s[3::2])   # 468

# # 14. for循环
# s = '123456789'
# for i in s:
#     print(i)



