#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import random
import os
STATUS = []

def get_md5(data):
    """
    md5加密数据
    :param data: 需要加密的数据
    :return: 加密后的数据
    """
    obj = hashlib.md5('adsfg12fsg'.encode('utf-8'))
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()


def get_data(length=4):
    """
    获取验证码
    :param length: 验证码长度
    :return: 验证码
    """
    data = []
    for i in range(length):
        v = chr(random.randint(65, 90)).lower()  # 得到一个随机数
        data.append(v)
    return ''.join(data)


def display_pages(arg):
    """
    页面展示功能
    :param arg:页面展示内容列表
    :return:
    """
    j = 1
    for i in arg:
        print(str(j) + '.', i)
        j += 1
    print()


def wrapper(func):
    def inner():
        if not STATUS:
            log_in()
        func()
    return inner


def log_in():
    while 1:
        name = input('请输入用户账号(N/n): ')
        if name.lower() == 'n':
            return
        pwd = get_md5(input('请输入密码: '))
        with open('user_list.txt', mode='r', encoding='utf-8') as f:
            flag = False
            a = False
            for i in f:
                if not i.strip():
                    print('用户不存在，请先注册')
                u, v = i.strip().split(':')
                if u == name and v == pwd:
                    val = get_data(4)
                    print(val)
                    while 1:
                        s = input('请输入验证码:')
                        if s != val:
                            continue
                        break
                    flag = True
                    print('恭喜您，登陆成功')
                    STATUS.append(name)
                    return
            if not flag:
                print('用户名或密码错误')


def user_register():
    while True:
        user_name = input('请输入注册用户名(N/n退出): ')
        if user_name.upper() == 'N':
            break
        if not os.path.exists('user_list.txt'):
            f = open('user_list.txt', mode='w', encoding='utf-8')
        else:
            f = open('user_list.txt', mode='r', encoding='utf-8')
            a = False
            for i in f:
                if not i.strip():
                    continue
                u, v = i.split(':')
                if user_name == u:
                    a = True
                    print('用户名已存在')
                    break
            if a:
                continue

        user_pwd = input('请输入密码: ')
        user_pwd2 = input('请确认密码: ')
        if user_pwd != user_pwd2:
            print('两次密码不一致')
            continue
        user_pwd = get_md5(user_pwd)

        # 把用户账号和密码写入文件
        f = open('user_list.txt', mode='a', encoding='utf-8')
        msg = user_name + ':' + user_pwd + '\n'
        f.write(msg)
        f.flush()
    f.close()


NEWS = {'1': {'prize': 0, 'comment': ''}}


def news_content():
    for i, j in NEWS.items():
        j = str(j).replace('{', '').replace('}', '')
        print(i, j)

@wrapper
def news_prize():
    while 1:
        name = input('输入要点赞的新闻：')
        if name.lower() == 'n':
            return
        if not NEWS.get(name):
            print('没有该新闻')
            continue
        NEWS[name]['prize'] += 1
        print(name, NEWS[name]['prize'])
        continue

@wrapper
def news_comment():
    while 1:
        name = input('输入要评价的新闻：')
        if name.lower() == 'n':
            return
        if not NEWS.get(name):
            print('没有该新闻')
            continue
        content = input('输入评价内容(N/n)：')
        NEWS[name]['comment'] += content
        print(name, NEWS[name]['comment'])
        continue


def news_list():
    news_li = ['新闻详情', '新闻点赞', '新闻评论']
    display_pages(news_li)
    while 1:
        choice = input('输入功能序号（N/n）：')
        if choice.lower() == 'n':
            return
        user_funcs = {'1': news_content, '2': news_prize, '3': news_comment}
        if not user_funcs.get(choice):
            print('输入有误，请重新输入')
            continue
        user_funcs.get(choice)()


def news_sys():
    li = ['用户登陆', '新闻列表']
    while 1:
        display_pages(li)
        choice = input('请选择功能序号(N/n):')
        if choice.lower() == 'n':
            return
        funcs = {'1': log_in, '2': news_list}
        if not funcs.get(choice):
            print('您的选择有误，请重新选择')
            continue
        funcs.get(choice)()


news_sys()


