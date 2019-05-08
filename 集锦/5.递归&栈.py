#!/usr/bin/env python
# -*- coding:utf-8 -*-

menu = {'北京':
        {'海淀': {'五道口': {
                'soho': {},
                '网易': {},
                'google': {}
                            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
                     },
            '上地': {
                '百度': {},
                    },
                },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

"""
递归实现
"""
# def threeLM(dic):
#     while True:
#         for k in dic:
#             print(k)
#         key = input('input>>').strip()
#         if key == 'b' or key == 'q':
#             return key
#         elif key in dic.keys() and dic[key]:
#             ret = threeLM(dic[key])
#             if ret == 'q':
#                 return 'q'
#
#
# threeLM(menu)

"""
堆栈实现
"""
# l = [menu]
# while l:
#     for key in l[-1]:
#         print(key)
#     k = input('input>>').strip()   # 北京
#     if k in l[-1].keys() and l[-1][k]:
#         l.append(l[-1][k])
#     elif k == 'b':
#         l.pop()
#     elif k == 'q':
#         break


"""
栈实现：计算文件夹大小
"""
import os
path = os.path.dirname(os.path.dirname(__file__))

li = [path]
size = 0
while li:
    path = li.pop()
    for i in os.listdir(path):
        i = os.path.join(path, i)
        if os.path.isdir(i):
            li.append(i)
        else:
            size += os.path.getsize(i)

print(size)




















