#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


def func(lnum, rnum, count):
    li = []
    i = 0
    while i < count:
        li.append(random.randint(lnum, rnum))
        i += 1
    return li

