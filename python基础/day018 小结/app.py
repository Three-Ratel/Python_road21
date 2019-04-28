#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime

SHOPPING_CAR = {}

# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 1000},
    {'id': 3, 'title': '大炮', 'price': 1000},
    {'id': 8, 'title': '迫击炮', 'price': 1000},
    {'id': 9, 'title': '手枪', 'price': 1000},
]


def run():
    # 购物车
    while True:
        for i in range(len(GOODS_LIST)):
            print(i + 1, GOODS_LIST[i]['title'])

        choice = input('请选择序号（N购买完成）:')
        if choice.upper() == 'N':
            # 购买完成之后，写入文件
            ctime = datetime.now().strftime('%Y-%m-%d')
            with open(ctime, mode='a', encoding='utf-8') as f:
                # {1: {'title': '飞机', 'price': 1000, 'count': 15}, 8: {'title': '迫击炮',\
                # 'price': 1000, 'count': 10}}
                for key, value in SHOPPING_CAR.items():
                    line = "%s|%s|%s|%s\n" % (key, value['title'], value['price'], value['count'],)
                    f.write(line)

            return

        choice = int(choice)
        number = int(input('购买数量:'))
        row_info = GOODS_LIST[choice - 1]
        if row_info['id'] in SHOPPING_CAR:
            SHOPPING_CAR[row_info['id']]['count'] = SHOPPING_CAR[row_info['id']]['count'] + number
        else:
            SHOPPING_CAR[row_info['id']] = {'title': row_info['title'],\
                                            'price': row_info['price'], 'count': number}
        print(SHOPPING_CAR)


if __name__ == '__main__':
    run()
