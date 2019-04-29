#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
3.发红包
    每一个人能够抢到的金额的概率都是平均的
    小数的不准确性的问题
"""
import random


class RedPackage(object):
    def __init__(self, money, people):
        self.money = money
        self.people = people

    def dispatch(self):
        money = self.money * 100
        data = set()
        while 1:
            val = random.randint(0, money)
            if val == money or val == 0:
                continue
            data.add(val)
            if len(data) == self.people - 1:
                break
        data = list(data)
        data.sort()
        data.insert(0, 0)
        li = []
        for i in range(1, len(data)):
            li.append(data[i] - data[i-1])
        last = money - sum(li)
        li.append(last)

        for i in range(len(li)):
            li[i] /= 100
        return li


RedPackage(100, 10).dispatch()


