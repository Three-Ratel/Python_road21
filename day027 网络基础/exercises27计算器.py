#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 9、大作业：计算器
"""
1)如何匹配最内层括号内的表达式
2)如何匹配乘除法
3)考虑整数和小数
4)写函数，计算‘23’ ‘10/5’
5)引用4)中写好的函数，完成'23/4'计算
"""
import re
s = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# s = input('输入：')
# print(eval(s))
s = s.replace(' ', '')
# print(s)

def mul_div(i):
    for j in i:
        if j.isdecimal() or j == '.':
            continue
        v = i.split(j)
        v.append(j)
        break

    if v[-1] == '/':
        val = float(v[0]) / float(v[1])
    elif v[-1] == '*':
        val = float(v[0]) * float(v[1])
    elif v[-1] == '+':
        val = float(v[0]) + float(v[1])
    elif v[-1] == '-':
        val = float(v[0]) - float(v[1])
    return val


def dispose_brcket(s):
    while True:
        data = re.search('\(-?[\d.]+\)', s)
        if not data:
            break
        data = data.group()
        new_data = data.strip('()')
        s = s.replace(data, new_data)
        s = s.replace('--', '+')
        s = s.replace('-+', '-')
        s = s.replace('+-', '-')
    return s


def add_mul(s):
    li = re.findall('\([^()]+\)', s)
    """
    第一个括号中的加减乘除
    """
    while True:
        try:
            i = li.pop()
        except:
            break

        """
        匹配第一个乘除法
        """
        while True:
            data = re.search('\d+(\.\d+)?[/*]\d+(\.\d+)?', i)
            if not data:
                break
            v = mul_div(data.group())
            new_i = i.replace(data.group(), str(v))
            s = s.replace(i, new_i)
            i = new_i

        """
        匹配第一个加减法
        """
        while True:
            data = re.search('\d+(\.\d+)?[-+]\d+(\.\d+)?', i)
            if not data:
                break
            v = mul_div(data.group())
            new_i = i.replace(data.group(), str(v))
            s = s.replace(i, new_i)
            i = new_i
    return s


def last_dispose(s):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', s)
        if not ret: break
        ret = ret.group()
        new_s = mul_div(ret)
        s = s.replace(ret, str(new_s))

    s = s.replace('--', '+')
    s = s.replace('+-', '-')
    s = s.replace('-+', '-')
    # return s

    while True:
        ret = re.search('-?\d+(\.\d+)?[-+]-?\d+(\.\d+)?', s)
        if not ret: break
        ret = ret.group()
        first = True
        for i in ret:
            if first:
                first = False
                continue
            if i == '-':
                new_ret = ret.split('-')
                print(new_ret)
                new_ret = float(new_ret[0]) - float(new_ret[1])
            else:
                new_ret = ret.split('+')
                print(new_ret)
                new_ret = float(new_ret[0]) + float(new_ret[1])

            s = s.replace(ret, str(new_ret))
            return s


def sub(s):
    while True:
        """
        处理当前最内层括号内的加减乘除
        """
        s = add_mul(s)
        """
        处理括号
        """
        s = dispose_brcket(s)
        print(s)
        if '(' not in s:
            s = last_dispose(s)
            return s

    # return s


val = sub(s)
print(val)