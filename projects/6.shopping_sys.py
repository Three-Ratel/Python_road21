#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
4.程序设计：用户管理系统
"""
import os
from datetime import datetime


def user_register():
    """
    用户注册功能
    content：要写入文件的内容
    users_list.txt：存放用户列表的文件
    :return: None
    """
    while True:
        user_name = input('please enter user name(N/n exit): ')
        if user_name.upper() == 'N':
            return
        f = open('users_list.txt', mode='a+', encoding='utf-8')
        f.seek(0)
        a = False
        for i in f:
            li = i.split(',')
            if li[0] == user_name:
                a = True
                print('用户已存在')
                break
        if a:
            continue

        while True:
            user_pwd = input('please enter your password: ')
            user_pwd2 = input('please ensure your password: ')
            if user_pwd != user_pwd2:
                continue
            rtime = datetime.now()
            rtime = rtime.strftime('%Y/%m/%d %H:%M:%S')
            break
        li = [user_name, user_pwd, rtime]
        content = ','.join(li)
        f = open('users_list.txt', mode='a+', encoding='utf-8')
        f.write(content + '\n')
        f.close()


def user_login():
    """
    flag：标记用户登陆是否成功
    info：存放用户登陆次数，如果次数为3则直接退出，并提示用户已经冻结
    :return:
    """
    flag = '用户名或密码错误'
    info = {}
    while True:
        log_name = input('please enter user name(N/n exit): ')
        if log_name.upper() == 'N':
            return
        """
        如果用户在BLACK_LIST中，直接退出
        """
        if os.path.exists('black_list.txt'):
            f = open('black_list.txt', mode='r', encoding='utf-8')
            for i in f:
                if i.strip() == log_name.strip():
                    print('该用户已冻结')
                    exit()

        if not os.path.exists('users_list.txt'):
            print('用户不存在，请重新输入')
            continue
        else:
            f = open('users_list.txt', mode='r', encoding='utf-8')
            a = False
            for i in f:
                u, v, w = i.strip().split(',')
                if u == log_name:
                    a = True
            if not a:
                print('用户不存在，请重新输入')
                continue

        log_pwd = input('please enter your pwd: ')
        f = open('users_list.txt', mode='r', encoding='utf-8')
        for i in f:
            u, v, w = i.strip().split(',')
            if u == log_name and v == log_pwd:
                flag = '登陆成功'
                STATUS.append(log_name)
                print(flag)
                return

        if info.get(log_name):
            info[log_name] = info[log_name] + 1
        else:
            info[log_name] = 1
        for u, v in info.items():
            if v == 3:
                f = open('black_list.txt', mode='a+', encoding='utf-8')
                u = u + '\n'
                f.write(u)
                f.close()
                print('用户已冻结')
                break
            else:
                print(flag)


def users_manage():
    """
    用户管理系统：
        1. 用户注册
        2. 用户登陆
    :return:
    """
    user_funs = {'1': user_register, '2': user_login}
    user_manu = ['用户注册', '用户登陆']

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
        return
    """
    功能选择
    """
    while True:
        display_pages(user_manu)
        num = input('please enter your choice(N/n): ')
        if num.upper() == 'N':
            return
        if not num.isdecimal():
            print('输入不合法，请重新输入')
            continue
        if not user_funs.get(num):
            print('输入不合法，请重新输入')
            continue
        user_funs.get(num)()


"""
# 5.有如下文件，请通过分页的形式将数据展示出来。【文件非常小】
"""


def goods_display(file_name='goods_list.txt'):
    if not os.path.exists(file_name):
        print('商品列表为空')
        return
    f = open(file_name, mode='r', encoding='utf-8')
    content = f.read()
    content_list = content.strip().split('\n')
    per_page_amount = 10
    content_list.pop(0)
    u, v = divmod(len(content_list), per_page_amount)
    u = u + 1 if v else u
    while True:
        num = input('please input the page(1-%s): ' % u)
        if num.upper() == 'N':
            return
        if not(num.isdecimal() and 0 < int(num) <= u):
            print('输入不合法，请重新输入')
            continue

        last_num = int(num) * per_page_amount -1
        begin_num = (int(num)-1) * per_page_amount
        new_content = content_list[begin_num: last_num+1]
        for i in new_content:
            print(i)
        f.close()


"""
7.程序设计：购物车
"""
# 购物车
SHOPPING_CAR = {}
# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 5000}, {'id': 3, 'title': '大炮', 'price': 3000},
    {'id': 8, 'title': '迫击炮', 'price': 2000}, {'id': 9, 'title': '手枪', 'price': 500}]


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
                price = str(GOODS_LIST[j]['price'])
                name_price = name + '|' + price
        """
        输入购买商品的数量
        """
        while True:
            count = input('请输入购买数量：')
            if not count.isdecimal():
                continue
            count = int(count)
            break

        if SHOPPING_CAR.get(name_price):
            SHOPPING_CAR[name_price] = SHOPPING_CAR[name_price] + count
        else:
            SHOPPING_CAR[name_price] = count

        i = os.path.dirname(os.path.abspath('shopping_sys.py'))
        file_path = '%s/shopping_car/%s/' % (i, STATUS[0])
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        v1 = datetime.now()
        y, m, d, H, M = v1.strftime('%Y/%m/%d/%H/%M').split('/')
        file_path = os.path.join(file_path + '%s-%s-%s-%s-%s.txt' % (y, m, d, H, M))

    """
    把购买信息写入文件，并保存
    """
    f = open(file_path, mode='a+', encoding='utf-8')
    for i in SHOPPING_CAR:
        s_goods = [i, str(SHOPPING_CAR[i])+'个']
        content = '|'.join(s_goods) + '\n'
        f.write(content)
        f.flush()
    f.close()
    return


"""
8.程序设计：沙河商城
功能：
    1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间写入到文件。
    2.用户登录，只有三次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已经冻结）。
    3.商品浏览，分页显示商品（小文件）； 用户可以选择商品且可以选择数量然后加入购物车（在全局变量操作），
      不再购买之后，需要讲购物车信息写入到文件，文件要写入到指定目录：
        shopping_car(文件夹)
            - 用户名A(文件夹)
                2019-11-11-09-59.txt
                2019-11-12-11-56.txt
                2019-12-11-11-47.txt
            - 用户B(文件夹)
                2019-11-11-11-11.txt
                2019-11-12-11-15.txt
                2019-12-11-11-22.txt
      注意：重复购买同一件商品时，只更改购物车中的数量。
    4.我的购物车，查看用户所有的购物车记录，即：找到shopping_car目录下当前用户所有的购买信息，并显示：
        2019-11-11-09-59.txt
            飞机|1000|10个
            大炮|2000|3个
        2019-11-12-11-56.txt
            迫击炮|10000|10个
            手枪|123|3个

    5.用户未登录的情况下，如果访问 商品浏览 、我的购物车 时，提示登录之后才能访问，让用户先去选择登录（装饰器实现）。
"""


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
    return


def shopping_car():
    i = os.path.dirname(os.path.abspath(__file__))
    file_path = '%s/shopping_car/%s/' % (i, STATUS[0])
    if not os.path.exists(file_path):
        print('用户没有购买信息')
        input('按enter键返回')
        return
    li = []
    for i in os.listdir(file_path):
        print(i)
        li.append(i)
    for i in li:
        print(i)
        goods_display(os.path.join(file_path, i))


def shopping_sys():
    li = ['用户注册', '用户登陆', '商品浏览', '购买商品', '我的购物车']
    funcs_list = {'1': user_register, '2': user_login, '3': goods_display, \
                  '4': buy_goods, '5': shopping_car}
    while True:
        display_pages(li)
        num = input('请输入功能选项(N/n): ')
        if num.upper() == 'N':
            if STATUS:
                STATUS.pop()
            exit()
        if not funcs_list.get(num):
            print('输入不合法，请重新输入')
            continue
        if num == '1' or num == '2':
            funcs_list.get(num)()
        else:
            if not STATUS:
                print('请先登陆，在进行操作')
                user_login()
                continue
            funcs_list.get(num)()


STATUS = []
shopping_sys()
