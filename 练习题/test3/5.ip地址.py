#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


def generate_ip():
    net = '172.25.254.'
    f = open('ip', mode='a+', encoding='utf-8')
    for i in range(100):
        v = random.randint(1, 254)
        ip = net + str(v) + '\n'
        f.write(ip)
    f.close()


def get_three():
    f = open('ip', mode='r', encoding='utf-8')
    ip_li = []
    for i in f:
        li = i.strip().rsplit('.')
        if len(li[-1]) == 3:
            ip_li.append(i.strip())
    return ip_li


def run():
    generate_ip()
    res = get_three()
    print(res)


run()
