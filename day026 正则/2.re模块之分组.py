#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
s = 'what are you doing? hahah, you would not understand 67678ah'
"""
分组之保留
"""

# # findall 遇上分组，只有你
# ret = re.findall('\d(\d)', s)
# print(ret)


"""
分组优先取消
"""
ret = re.findall('\d(?:\d)', s)
print(ret)


# # split 遇上分组，留下你
# # 会有空白产生，可以使用remove除去
# ret = re.split('(\d)', s)
# print(ret)


"""
分组之取出
"""
# s = '<h1>wahahahahaha</h1>'
# ret = re.findall('<\w+>(.*?)</\w+>', s)
# print(ret)


# s = '<h1>wahahahahaha</h1>'
# ret = re.search('<\w+>(.*?)</\w+>', s)
# print(ret.group(1))

"""
分组命名
"""
# s = '<h1>wahahahahaha</h1>'
# ret = re.search('<\w+>(?P<tag>.*?)</\w+>', s)
# print(ret.group('tag'))


"""
分组引用
"""
# s = '<h1>wahahahahaha</h1>'
# ret = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>', s)
# print(ret.group('tag'))



