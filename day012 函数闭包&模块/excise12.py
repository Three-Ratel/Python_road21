#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
作业（一）
1.学习笔记：md文件
2.思维导图：png文件
3.本周每天的作业（考试题）
"""


"""
作业（二）
1.写出三元运算的基本格式及作用？
"""
# v = a if 条件判断 else b


"""
2.什么是匿名函数？
"""
# lambda 又称为匿名函数


"""
3.尽量多的列举你了解的内置函数？【默写】
"""
# 输入输出：print，input
# 强制转换：int, str, list, tuple, dict, set
# 数学相关：abs, max, min, sum, float, divmod
# 进制转换：bin, oct, int, hex
# 其他：len, range, type, id, open
# map, filter, reduce
# chr ord

"""
4.filter / map / reduce函数的作用分别是什么？
"""
# map(func,v):map会循环取出v中的元素，作为参数传给func进行操作，追加到一个新list中，list 中元素和v中元素相等
# filter(func,v):filter 会循环取出v中的元素，作为参数传给func进行操作，追加到一个新list中，list中的元素会< v中元素
# reduce(func,v):reduce 会循环取出v中的元素，作为参数传给func进行操作，输出一个元素

"""
5.看代码写结果
"""
# def func(*args, **kwargs):
#     print(args, kwargs)
# a. 执行 func(12,3,*[11,22]) ，输出什么？
# b. 执行 func(('alex','武沛齐',),name='eric')

# 12，3 11， 22
# {}
# (('alex', '武沛齐'),)
# {'name': 'eric'}

"""
6.看代码分析结果
"""
# def func(arg):
#     return arg.pop(1)
#
# result = func([11, 22, 33, 44])
# print(result)
# 22




"""
7.看代码分析结果
"""
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda: i)
#
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1, v2)
# 9, 9



"""
8.看代码分析结果
"""
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1, v2)
# 11
# 10



"""
9.看代码分析结果
"""
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for i in range(0, len(func_list)):
#     result = func_list[i](i)
#     print(result)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18


"""
10.看代码分析结果
"""
# def f1():
#     print('f1')
#
# def f2():
#     print('f2')
#     return f1
#
# func = f2()
# result = func()
# print(result)
# f2
# f1
# None



"""
11.看代码分析结果【面试题】
"""
# def f1():
#     print('f1')
#     return f3()
#
# def f2():
#     print('f2')
#     return f1
#
# def f3():
#     print('f3')
#
# func = f2()
# result = func()
# print(result)
# f2
# f1
# f3
# None



"""
12.看代码分析结果
"""

# name = '景女神'
#
# def func():
#     def inner():
#         print(name)
#     return inner()
#
# v = func()
# print(v)
# '景女神'
# None


"""
13.看代码分析结果
"""
# name = '景女神'
# def func():
#     def inner():
#         print(name)
#         return "老男孩"
#     return inner()
#
# v = func()
# print(v)
# '景女神'
# "老男孩"




"""
14.看代码分析结果
"""

# name = '景女神'
#
# def func():
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v = func()
# result = v()
# print(result)
# '景女神'
# "老男孩"





"""
15.看代码分析结果
"""

# def func():
#     name = '武沛齐'
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v1 = func()
# v2 = func()
# print(v1, v2)
# v1, v2都是inner函数的地址




"""
16.看代码写结果
"""

# def func(name):
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v1 = func('金老板')
# v2 = func('alex')
# print(v1, v2)
# v1, v2都是inner函数的地址





"""
17.看代码写结果
"""

# def func(name=None):
#     if not name:
#         name = '武沛齐'
#     def inner():
#         print(name)
#         return '老男孩'
#     return inner
#
# v1 = func()
# v2 = func('alex')
# print(v1, v2)
# v1, v2都是inner函数的地址





"""
18.看代码写结果【面试题】
"""
# def func(name):
#     v = lambda x: x + name
#     return v
#
# v1 = func('武沛齐')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1, v2, v3, v4)
# v1, v2都是lambda函数的地址
# 银角武沛齐 金角alex




"""
19.看代码写结果
"""
# NUM = 100
# result = []
# for i in range(10):
#     func = lambda: NUM  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
# 9
# 10个lambda地址
# 100
# 100





"""
20.代码写结果【面试题】
"""
# result = []
# for i in range(10):
#     func = lambda: i  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
# 9
# 10个lambda地址
# 9
# 9


"""
21.看代码分析结果【面试题】
"""
# def func(num):
#     def inner():
#         print(num)
#     return inner
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)

# 9
# 10个inner地址
# 0
# 9
# None
# None





"""
22.
程序设计题

> 请设计实现一个商城系统，商城主要提供两个功能：商品管理、会员管理。
> 商品管理
> - 查看商品列表
> - 根据关键字搜索指定商品
> - 录入商品
> 会员管理：【无需开发，如选择则提示此功能不可用，正在开发中，让用户重新选择】
"""

#需求细节：
# 1.启动程序让用户选择进行商品管理或会员管理，如：
# 2.用户选择 【1】 则进入商品管理页面，进入之后显示商品管理相关的菜单，如：
# 3.用户选择【2】则提示此功能不可用，正在开发中，让用户重新选择。
# 4.如果用户在【商品管理】中选择【1】，则按照分页去文件goods.txt中读取所有商品，并全部显示出来【分页功能可选】。
# 5.如果用户在【商品管理】中选择【2】，则让提示让用户输入关键字，输入关键字后根据商品名称进行模糊匹配，如：
# 6.如果用户在【商品管理】中选择【3】，则提示让用户输入商品名称、价格、数量然后写入到 goods.txt文件

"""
用户注册和登陆
"""
import hashlib

"""
md5加密
"""
def get_data_md5(data):
    obj = hashlib.md5()
    obj.update(str(data).strip('[]{}()').encode('utf-8'))
    v = obj.hexdigest()
    return v


"""
用户登陆
"""
def user_log_on():
    flag = "登陆失败"
    name = input('请输入管理员账号: ')
    pwd = get_data_md5(input('请输入管理员密码: '))
    with open('user_list.txt', mode='r', encoding='utf-8') as f:
        if len(f.readlines(1)) == 0:
            flag = "用户列表为空文件"
            print(flag)
            return flag
        for i in f:
            u, v = i.strip().split(':')
            if name == u and pwd == v:
                flag = '登陆成功'
                print(flag)
                return flag
    print(flag)
    return flag

"""
商品管理系统
"""
def mall_manage():
    TITLE = ['欢迎使用老子的购物商城', '【商品管理】', '【商品列表】', '【录入商品】', '【根据关键字搜索】', '【会员管理】']
    FAULT = "输入不合法，请重新输入"
    PER_PAGE_AMOUNT = 10
    FILE = 'goods.txt'

    """
    1.展示页面
    """
    def display_pages(arg):
        j = 1
        for i in arg:
            print(str(j) + '.', i)
            j += 1
        print()
        print('请选择（输入N返回上一级):')
        return
    """
    2.判断用户输入
    """
    def just_user_input(num, li=None):
        if num.upper() == 'N':
            return 'N'
        # 判断输入是否是可迭代对象的索引
        elif num.isdecimal() and 0 < int(num) <= len(li):
            num = int(num) - 1
            return num
        # 判断输入不是空格，回车等字符
        elif len(num.strip()):
            return FAULT
        else:
            return FAULT
        # 不合法都返回falut

    """
    3.商品管理
    """
    def goods_manage():
        goods_list = ['查看商品列表', '根据关键字搜索指定商品', '录入商品']
        s = '******' + ''.join(TITLE[:2]) + '******'

        """
        1.查看商品列表
        """
        def check_goods_list(filename):
            print('******' + ''.join(TITLE[0:3]) + '******')
            with open(filename, mode='r', encoding='utf-8') as f:
                if f.readlines(1):
                    pass
                else:
                    print('没有商品')
                    input('按任意键继续')
                    return
                msg = 1
                for i in f:
                    u, v, w = i.strip().split(':')
                    print(u, ' ', v, ' ', w, ' ')
                    msg += 1
                    if msg == PER_PAGE_AMOUNT + 1:
                        msg = 1
                        input('按enter显示下一页')
                input('按任意键返回')
                return

        """
        2.根据关键字搜索指定商品
        """
        def check_goods_keys(filename):
            print('******' + ''.join(TITLE[:2]) + TITLE[4] + '******')
            flag = False
            while True:
                key = input('输入关键字输入N返回: ')
                if key.upper() == 'N':
                    break
                elif len(key.strip()) == 0:
                    print(FAULT)
                    continue
                else:
                    pass
                with open(filename, mode='r', encoding='utf-8') as f:
                    msg = 1
                    print('***搜索结果如下***')
                    for i in f:
                        u, v, w = i.strip().split(':')
                        if key in u:
                            flag = True
                            print(u, ' ', v, ' ', w, ' ')
                            msg += 1
                            if msg == PER_PAGE_AMOUNT + 1:
                                msg = 1
                                input('按enter显示下一页')
                                print('***搜索结果如下***')

                    if not flag:
                        print('没有该商品')
            return

        """
        3.录入商品
        """
        def check_goods_in(filename):
            print('******' + ''.join(TITLE[:2]) + TITLE[3] + '******')
            while True:
                """
                输入商品名称
                """
                while True:
                    good_name = input('请输入商品名称(输入N返回上一级)：')
                    if len(good_name.strip()) == 0:
                        print(FAULT)
                        continue
                    f = open(filename, mode='a', encoding='utf-8')
                    if good_name.upper() == 'N':
                        f.close()
                        return
                    break
                """
                输入商品价格
                """
                while True:
                    good_price = input('请输入商品价格：')
                    if len(good_price.strip()) == 0:
                        print(FAULT)
                        continue
                    break

                """
                输入商品数量
                """
                while True:
                    good_amount = input('请输入商品数量：')
                    if len(good_name.strip()) == 0 or not good_amount.isdecimal():
                        print(FAULT)
                        continue
                    break
                li = [good_name, good_price, good_amount]
                f.write(':'.join(li) + '\n')
                f.flush()
                print('添加成功')
                f.close()
                return

        while True:
            print(s)
            display_pages(goods_list)
            goods_funcs = [check_goods_list, check_goods_keys, check_goods_in]
            num = input('please input your choice: ')
            v = just_user_input(num, goods_list)
            if v == 'N':
                return
            elif v == FAULT:
                print(v)
            else:
                goods_funcs[v](FILE)

    """
    4.会员管理
    """
    def users_manage():
        PER_PAGE_AMOUNT = 10
        print('******' + TITLE[0]+TITLE[5] + '******')
        users_manage_list = ['添加用户', '用户列表', '修改密码', '删除用户']
        display_pages(users_manage_list)

        """
        1.1用户注册
        """
        def user_add():
            while True:
                print('******' + TITLE[0] +'【会员管理】' + '【' + users_manage_list[0] + '】' + '******')
                user_name = input('输入用户名(N退出): ')
                if user_name.upper() == 'N':
                    break
                if user_name.strip() == '':
                    print('不合法用户名')
                    continue
                """
                判断用户是否存在，不存在继续，存在则重新输入
                """
                with open('user_list.txt', mode='r', encoding='utf-8') as f:
                    if len(f.readlines(1)) == 1:
                        a = True
                        with open('user_list.txt', mode='r', encoding='utf-8') as f:
                            for i in f:
                                u, v = i.split(':')
                                if user_name == u:
                                    a = False
                                    print('用户名已存在')
                                    break
                            if a:
                                pass
                            else:
                                continue
                    else:
                        pass

                """
                用户设置密码，并加密
                """
                while True:
                    user_pwd = input('请输入密码: ')
                    user_pwd2 = input('请确认密码: ')
                    if user_pwd != user_pwd2:
                        print('两次密码不一致')
                        continue
                    else:
                        break
                user_pwd = get_data_md5(user_pwd)

                """
                把用户账号和密码写入文件
                """
                f = open('user_list.txt', mode='a', encoding='utf-8')
                msg = user_name + ':' + user_pwd + '\n'
                f.write(msg)
                f.flush()
            f = open('user_list.txt', mode='a', encoding='utf-8')
            f.close()
        """
        1.2用户列表
        """
        def users_list():
            print('******' + TITLE[0] + '【会员管理】' + '【' + users_manage_list[1] + '】' + '******')
            with open('user_list.txt', mode='r', encoding='utf-8') as f:
                if len(f.readlines(1)) == 1:
                    with open('user_list.txt', mode='r', encoding='utf-8') as f:
                        j = 1
                        for i in f:
                            u, v = i.split(':')
                            print(u)
                            j += 1
                            if j == PER_PAGE_AMOUNT +1:
                                j = 1
                                input('按enter继续')
                else:
                    print('没有用户')
                input('按enter结束')
                return
        """
        1.3修改密码
        """
        def modify_user_pwd():
            while True:
                print('******' + TITLE[0] + '【会员管理】' + '【' + users_manage_list[2] + '】' + '******')
                user_name = input('输入用户名(N退出): ')
                if user_name.upper() == 'N':
                    break
                if user_name.strip() == '':
                    print('不合法用户名')
                    continue

                with open('user_list.txt', mode='r', encoding='utf-8') as f:
                    a = '用户不存在'
                    for i in f:
                        u, v = i.strip().split(':')
                        if user_name != u:
                            pass
                        else:
                            a = True
                    if a == '用户不存在':
                        print(a)
                        continue
                    else:
                        with open('user_list.txt', mode='r', encoding='utf-8') as f, \
                                open('user_list1.txt', mode='w', encoding='utf-8') as f1:
                            if len(f.readlines(1)) == 1:
                                with open('user_list.txt', mode='r', encoding='utf-8') as f:
                                    for i in f:
                                        u, v = i.strip().split(':')
                                        if user_name == u:
                                            while True:
                                                user_pwd = input('请输入密码: ')
                                                user_pwd2 = input('请确认密码: ')
                                                if user_pwd != user_pwd2:
                                                    print('两次密码不一致')
                                                    continue
                                                else:
                                                    break
                                            user_pwd = get_data_md5(user_pwd)

                                            f1.write(user_name + ':' + user_pwd + '\n')
                                        else:
                                            f1.write(i)
                                            f1.flush()
                        # 删除旧文件，并重新命名新文件
                        import os
                        os.remove('user_list.txt')
                        os.rename('user_list1.txt', 'user_list.txt')
            return
        """
        1.4删除用户
        """
        def user_del():
            while True:
                print('******' + TITLE[0] + '【会员管理】' + '【' + users_manage_list[3] + '】' + '******')
                user_name = input('输入用户名(N退出): ')
                if user_name.upper() == 'N':
                    break
                if user_name.strip() == '':
                    print('不合法用户名')
                    continue

                with open('user_list.txt', mode='r', encoding='utf-8') as f:
                    a = '不存在'
                    for i in f:
                        u, v = i.strip().split(':')
                        if user_name != u:
                            pass
                        else:
                            a = True
                    if a == '不存在':
                        print(a)
                        continue

                with open('user_list.txt', mode='r', encoding='utf-8') as f, \
                        open('user_list1.txt', mode='w', encoding='utf-8') as f1:
                    if len(f.readlines(1)) == 1:
                        with open('user_list.txt', mode='r', encoding='utf-8') as f:
                            for i in f:
                                u, v = i.strip().split(':')
                                if user_name == u:
                                    print('用户已删除')
                                else:
                                    f1.write(i)
                                    f1.flush()
                # 删除旧文件，并重新命名新文件
                import os
                os.remove('user_list.txt')
                os.rename('user_list1.txt', 'user_list.txt')
                return
        ''
        while True:
            print('******' + TITLE[0] + '】' + TITLE[5] + '】******')
            users_manage_funcs = [user_add, users_list, modify_user_pwd, user_del]
            display_pages(users_manage_list)
            num = input('请选择输入N返回: ')
            v = just_user_input(num, users_manage_funcs)
            if v == "N":
                return
            elif v == FAULT:
                print(v)
            else:
                users_manage_funcs[v]()

    """
    5. 首页展示
    """
    while True:
        print('******', TITLE[0], '******')
        li = ['商品管理', '会员管理']
        display_pages(li)
        num = input('please input your choice: ')
        funcs = [goods_manage, users_manage]
        v = just_user_input(num, li)
        if v == 'N':
            break
        elif v == FAULT:
            print(v)
        else:
            funcs[v]()

# mall_manage() if user_log_on() == '登陆成功' else exit()
mall_manage()





