#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
    TITLE = ['欢迎使用老子的购物商城', '【商品管理】', '【商品列表】', \
    '【录入商品】', '【根据关键字搜索】', '【会员管理】']
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