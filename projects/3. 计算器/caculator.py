#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import functools

exp = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
exp = exp.replace(' ', '')


def div_mul(exp):
    patt = re.compile('\d+(\.\d+)?[*/]-?\d+(\.\d+)?')
    while True:
        no_bracket = patt.search(exp)
        if not no_bracket: break
        no_bracket = no_bracket.group()
        if '*' in no_bracket:
            a, b = no_bracket.split('*')
            val = float(a) * float(b)
        else:
            a, b = no_bracket.split('/')
            val = float(a) / float(b)
        exp = exp.replace(no_bracket, str(val))
    return exp


def exp_format(exp):
    exp = str(exp)
    exp = exp.replace('--', '+')
    exp = exp.replace('-+', '-')
    exp = exp.replace('+-', '-')
    return exp


def add_duc(exp):
    li = re.findall('[-+]?\d+(?:\.\d+)?', exp)
    if not li: return exp
    val = functools.reduce(lambda x, y: float(x) + float(y), li)
    return val


def cal(exp):
    sub_exp = div_mul(exp)
    sub_exp = exp_format(sub_exp)
    return add_duc(sub_exp)


pattern = re.compile('\([^()]+\)')
while True:
    no_brackets = pattern.search(exp)
    if not no_brackets: break
    no_brackets = no_brackets.group()
    exp = exp.replace(no_brackets, str(cal(no_brackets)))

res = cal(exp)
print(res)
