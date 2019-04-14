#!/usr/bin/env python
# -*- coding:utf-8 -*-

# with open('a.txt', mode='r', encoding='utf-8') as f1, open('b.txt', mode='w', encoding='utf-8') as f2:
#     for line in f1.readlines():
#         line = line.replace('a', 'b')
#         f2.write(line)


with open('a.txt', mode='r', encoding='utf-8') as f1:

    li = []
    for i in f1:
        print(i)
    #     li.append(i)
    # print(li)
    print('------------------------------------')
    f1.seek(0)
    for line in f1.readlines():
        print(line)
