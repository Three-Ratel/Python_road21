# !/usr/bin/env python
# -*- coding:utf-8 -*-


def read_content():
    per_page_amount = 3
    f = open('goods_list.txt', mode='r', encoding='utf-8')
    count = 0
    for i in f:
        count += 1
    f.close()
    u, v = divmod(count, per_page_amount)
    u = u + 1 if v else u
    while True:
        li = []
        num = input('please enter a pages(1-%s): ' % u)
        if num.upper() == 'N':
            return
        if not num.isdecimal():
            print('输入不合法')
            continue

        if not 0 < int(num) <= u:
            print('输入不合法')
            continue

        last_pages = (int(num)-1) * (per_page_amount)
        index = 0
        with open('goods_list.txt', mode='r', encoding='utf-8') as f:
            for i in f:
                index += 1
                if last_pages < index <= last_pages + per_page_amount:
                    li.append(i.strip())
                    continue
            c = 1
            for i in li:
                print(c, i)
                c += 1




