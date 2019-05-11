#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from functools import reduce


def exp_format(exp):
    exp = exp.replace('--', '+')
    exp = exp.replace('+-', '-')
    exp = exp.replace('++', '+')
    exp = exp.replace('-+', '-')
    return exp


def mul_div(atom_exp):  # 最基础的两个数的加减乘除
    if '*' in atom_exp:
        a, b = atom_exp.split('*')
        res = float(a) * float(b)
    else:
        a, b = atom_exp.split('/')
        res = float(a) / float(b)
    return res


def cal_muldiv(exp):  # 匹配乘除法 计算
    com = re.compile('\d+(\.\d+)?[*/]-?\d+(\.\d+)?')
    while True:
        obj = com.search(exp)
        if obj:
            atom_exp = obj.group()
            res = mul_div(atom_exp)
            exp = exp.replace(atom_exp, str(res))
        else:
            break
    return exp


def cal_addsub(exp):  # 计算加减法
    ret = re.findall('[-+]?\d+(?:\.\d+)?', exp)
    count = reduce(lambda x, y: float(x) + float(y), ret)
    return count


def cal(non_bracket):
    sub_exp = cal_muldiv(non_bracket)
    sub_exp = exp_format(sub_exp)
    ret = cal_addsub(sub_exp)
    return ret


exp = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 算式的去空格
exp = exp.replace(' ', '')


def main(exp):
    while True:
        ret = re.search('\([^()]+\)', exp)
        if ret: non_bracket = ret.group()
        else: return exp
        ret = cal(non_bracket)
        exp = exp.replace(non_bracket, str(ret))
        exp = exp_format(exp)


exp = main(exp)
ret = cal(exp)
print(ret)

# 去括号
# 把括号表达式匹配出来，调用上面的这个逻辑
