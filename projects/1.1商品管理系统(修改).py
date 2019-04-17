#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
"""
用户注册和登陆
"""
"""
md5加密
"""


def get_data_md5(data):
    s = 'ad12,ghj*\'kl\'dfghjdfghjkhjvbjhuy78e32314sfdxAAERTYUv/./jub'
    v = hashlib.md5((s + str(data).strip('{}[]()')).encode('utf-8'))
    return v.hexdigest()


"""
判断文件是否为空
"""


def just_file_empty(filename):
    with open(filename, mode='a+') as f:
        f.seek(0)
        v = len(f.readline().strip())
        return v


"""
用户登陆
"""


def user_log_on(users_txt):
    flag = "登陆失败：用户名或密码错误"
    with open(users_txt, mode='r', encoding='utf-8') as f:
        if not just_file_empty(users_txt):
            print("用户列表为空文件,请先注册用户")
            return
        name = input('请输入管理员账号: ')
        pwd = get_data_md5(input('请输入管理员密码: '))
        for i in f:
            u, v = i.strip().split(':')
            if name == u and pwd == v:
                flag = '登陆成功'
                print(flag)
                return True
    print(flag)
    return


"""
公共展示页面
"""


def display_pages(data_list):
        j = 1
        for i in data_list:
            print(str(j) + '.', i)
            j += 1
        print()
        return


"""
二级：商品管理
"""


def goods_manage():
    goods_list = ['查看商品列表', '根据关键字搜索指定商品', '录入商品']
    s = '******' + ''.join(TITLE[:2]) + '******'
    """
    1.1 查看商品列表
    """
    def check_goods_list(filename):
        print('******' + ''.join(TITLE[0:3]) + '******')
        if just_file_empty(filename):
            with open(filename, mode='r', encoding='utf-8') as f:
                msg = 1
                for i in f:
                    u, v, w = i.strip().split(':')
                    print(u, ' ', v, ' ', w, ' ')
                    msg += 1
                    if msg == PER_PAGE_AMOUNT + 1:
                        msg = 1
                        input('按enter显示下一页')
                input('按enter键返回')
        else:
            print('没有商品')
        return

    """
    1.2 根据关键字搜索指定商品
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
    1.3 录入商品
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
            continue

    """
    首页展示
    """
    while True:
            print(s)
            display_pages(goods_list)
            goods_funcs = {'1': check_goods_list, '2': check_goods_keys, '3': check_goods_in}
            num = input('请选择（输入N返会上一级）: ')
            if num.upper() == 'N':
                return
            if not goods_funcs.get(num):
                print(FAULT)
                continue
            goods_funcs[num](FILE)


"""
二级：会员管理
"""


def users_manage():
    """
    2.1添加用户
    """

    def user_add(filename):
        print(s)
        while True:
            user_name = input('输入用户名(N退出): ')
            if user_name.upper() == 'N':
                break
            if user_name.strip() == '':
                print('不合法用户名')
                continue
            """
            判断用户是否存在，不存在继续，存在则重新输入
            """
            if just_file_empty(filename):
                with open(filename, mode='r', encoding='utf-8') as f:
                    for i in f:
                        a = False
                        u, v = i.split(':')
                        if user_name == u:
                            a = '用户名已存在'
                            print(a)
                            break
                    if a:
                        continue
            """
            用户设置密码，并加密
            """
            while True:
                user_pwd = input('请输入密码: ')
                user_pwd2 = input('请确认密码: ')
                if user_pwd != user_pwd2:
                    print('两次密码不一致')
                    continue
                break
            user_pwd = get_data_md5(user_pwd)

            """
            把用户账号和密码写入文件
            """
            f = open(filename, mode='a', encoding='utf-8')
            msg = user_name + ':' + user_pwd + '\n'
            f.write(msg)
            f.flush()
        f = open(filename, mode='a', encoding='utf-8')
        f.close()

    """
    2.2用户列表
    """

    def users_list(filename):
        print(s)
        if just_file_empty(filename) == 0:
            print('没有用户')
            input('按enter返回')
            return
        with open(filename, mode='r', encoding='utf-8') as f:
            j = 1
            for i in f:
                u, v = i.split(':')
                print(u)
                j += 1
                if j == PER_PAGE_AMOUNT + 1:
                    j = 1
                    input('按enter继续')
        input('按enter返回')
        return

    """
    2.3修改密码
    """

    def modify_pwd(filename):
        while True:
            print(s)
            user_name = input('输入用户名(N退出): ')
            if user_name.upper() == 'N':
                break
            if user_name.strip() == '':
                print('不合法用户名')
                continue

            # 判断用户是否存在
            with open(filename, mode='r', encoding='utf-8') as f:
                a = '用户不存在'
                for i in f:
                    u, v = i.strip().split(':')
                    if user_name == u:
                        a = True
                if a == '用户不存在':
                    print(a)
                    continue

            with open(filename, mode='r', encoding='utf-8') as f, \
                    open('users_list1.txt', mode='w', encoding='utf-8') as f1:
                for i in f:
                    u, v = i.strip().split(':')
                    if user_name == u:
                        # 用户输入新密码
                        while True:
                            user_pwd = input('请输入密码: ')
                            user_pwd2 = input('请确认密码: ')
                            if user_pwd != user_pwd2:
                                print('两次密码不一致')
                                continue
                            break
                        user_pwd = get_data_md5(user_pwd)
                        f1.write(user_name + ':' + user_pwd + '\n')
                    else:
                        f1.write(i)
                        f1.flush()
                # 删除旧文件，并重新命名新文件
                import os
                os.remove(filename)
                os.rename('users_list1.txt', filename)
        return

    """
    2.4删除用户
    """

    def users_del(filename):
        while True:
            print(s)
            user_name = input('输入用户名(N退出): ')
            if user_name.upper() == 'N':
                break
            if user_name.strip() == '':
                print('不合法用户名')
                continue
            if not just_file_empty(filename):
                print('用户文件列表为空')
            with open(filename, mode='r', encoding='utf-8') as f, \
                    open('user_list1.txt', mode='w', encoding='utf-8') as f1:
                a = '不存在'
                for i in f:
                    u, v = i.strip().split(':')
                    if user_name != u:
                        f1.write(i)
                        f1.flush()
                        continue
                    print('用户已删除')
                    a = 1

                if a == '不存在':
                    print(a)
                    continue
            # 删除旧文件，并重新命名新文件
            import os
            os.remove(filename)
            os.rename('user_list1.txt', filename)
            continue

    users_manage_funcs = {'1': user_add, '2': users_list, '3': modify_pwd, '4': users_del}
    users_manage_list = ['添加用户', '用户列表', '修改密码', '删除用户']
    vip_title_list = []
    for i in users_manage_list:
        i = '【' + i + '】'
        vip_title_list.append(i)

    """
    会员首页展示
    """
    while True:
        vip_title = TITLE[0] + TITLE[5]
        print('******' + vip_title + '******')
        display_pages(users_manage_list)
        num = input('请选择输入N返回: ')
        if num.upper() == "N":
            return
        if not users_manage_funcs.get(num):
            print(FAULT)
            continue
        s = '******' + vip_title + vip_title_list[int(num)-1] + '******'
        users_manage_funcs[num](USER_FILE)





def mall_manage_sys():
    """
    商品管理系统
    """
    while True:
        print('******', TITLE[0], '******')
        li = ['商品管理', '会员管理']
        display_pages(li)
        num = input('请选择（输入N退出）: ')
        if num.upper() == "N":
            return
        funcs = {'1': goods_manage, '2': users_manage}
        if not funcs.get(num):
            print(FAULT)
            continue

        funcs[num]()


TITLE = ['欢迎使用老子的购物商城', '【商品管理】', '【商品列表】', '【录入商品】', '【根据关键字搜索】', '【会员管理】']
FAULT = "输入不合法，请重新输入"
FILE = 'goods.txt'
USER_FILE = 'users_list.txt'
PER_PAGE_AMOUNT = 10


mall_manage_sys() if user_log_on(USER_FILE) else exit(0)

"""
用户名：henry
密码：123
"""