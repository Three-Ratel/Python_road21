#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
7.程序设计：购物车
"""

"""
有如下商品列表 GOODS_LIST，用户可以选择进行购买商品并加入到购物车 SHOPPING_CAR 
中且可以选择要购买数量，购买完成之后将购买的所有商品写入到文件中【文件格式为：年_月_日.txt】。

注意：重复购买同一件商品时，只更改购物车中的数量。
"""
# 购物车
SHOPPING_CAR = {}

# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 1000},
    {'id': 3, 'title': '大炮', 'price': 1000},
    {'id': 8, 'title': '迫击炮', 'price': 1000},
    {'id': 9, 'title': '手枪', 'price': 1000},
]


# 购物车
SHOPPING_CAR = {}

# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 1000},
    {'id': 3, 'title': '大炮', 'price': 1000},
    {'id': 8, 'title': '迫击炮', 'price': 1000},
    {'id': 9, 'title': '手枪', 'price': 1000},
]
from datetime import datetime

def buy_goods():
    # li 把商品的id存放到li中
    li = []
    for i in range(len(GOODS_LIST)):
        print(GOODS_LIST[i]['id'], GOODS_LIST[i]['title'], GOODS_LIST[i]['price'])
        li.append(str(GOODS_LIST[i]['id']))
    # 把指定商品加入购物车

    while True:
        num = input('请输入要购买商品的id(N/n)：')
        if num.upper() == 'N':
            break
        if num not in li:
            print('输入不合法')
            continue

        for j in range(len(GOODS_LIST)):
            if GOODS_LIST[j]['id'] == int(num):
                name = str(GOODS_LIST[j]['title'])
        while True:
            count = input('请输入购买数量：')
            if not count.isdecimal():
                continue
            count = int(count)
            break
        if SHOPPING_CAR.get(name):
            SHOPPING_CAR[name] = SHOPPING_CAR[name] + count
        else:
            SHOPPING_CAR[name] = count

    v1 = datetime.now()
    y, m, d, h, m = v1.strftime('%Y/%m/%d/%H/%M').split('/')
    file_name = '%s-%s-%s-%s-%s.txt' % (y, m, d, h, m)
    f = open(file_name, mode='a+', encoding='utf-8')
    for i in SHOPPING_CAR:
        content = i + ',' + str(SHOPPING_CAR[i]) + '\n'
        f.write(content)
        f.flush()
    f.close()



