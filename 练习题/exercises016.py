"""
1.列举你常见的内置函数。
"""
# 类型转换：int, bool, list, tuple, dict, set
# 数学相关：abs, max, min, float, round, divmod
# 进制转换：bin, oct, int, hex
# 函数相关：map, filter, reduce
# 编码相关：chr, ord
# 其他:range, len, type, id,

"""
2.列举你常见的内置模块？
"""
# copy
# hashlib
# getpass
# random
# time
# datetime
# os
# sys
# json
# pickle
# shutil


"""
3.json序列化时，如何保留中文？
"""
# import json
# v = "你好"
# val = json.dumps(v, ensure_ascii=False)
# print(val)

"""
4.程序设计：用户管理系统
功能：
    1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间写入到文件。
    2.用户登录，只有三次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已经冻结）。
"""
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
    import os
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
                    return

        log_pwd = input('please enter your pwd: ')
        f = open('users_list.txt', mode='r', encoding='utf-8')
        for i in f:
            if not i.strip():
                print('用户列表为空')
            u, v, w = i.strip().split(',')
            if u == log_name and v == log_pwd:
                flag = '登陆成功'
                print(flag)
                return
        print(flag)
        if info.get(log_name):
            info[log_name] = info[log_name] + 1
        else:
            info[log_name] = 1
        print(info)
        for u, v in info.items():
            if v == 3:
                f = open('black_list.txt', mode='a+', encoding='utf-8')
                u = u + '\n'
                f.write(u)
                f.close()
                print('用户已冻结')
                break

user_login()


"""
5.有如下文件，请通过分页的形式将数据展示出来。【文件非常小】
商品 | 价格
飞机 | 1000
大炮 | 2000
迫击炮 | 1000
手枪 | 123
"""
# def read_content():
#     per_page_amount = 3
#     f = open('goods_list.txt', mode='r', encoding='utf-8')
#     count = 0
#     for i in f:
#         count += 1
#     f.close()
#     u, v = divmod(count, per_page_amount)
#     u = u + 1 if v else u
#     while True:
#         li = []
#         num = input('please enter a pages(1-%s): ' % u)
#         if num.upper() == 'N':
#             return
#         if not num.isdecimal():
#             print('输入不合法')
#             continue
#
#         if not 0 < int(num) <= u:
#             print('输入不合法')
#             continue
#
#         last_pages = (int(num)-1) * (per_page_amount)
#         index = 0
#         with open('goods_list.txt', mode='r', encoding='utf-8') as f:
#             for i in f:
#                 index += 1
#                 if last_pages < index <= last_pages + per_page_amount:
#                     li.append(i.strip())
#                     continue
#             c = 1
#             for i in li:
#                 print(c, i)
#                 c += 1
#
# read_content()


"""
6.有如下文件，请通过分页的形式将数据展示出来。【文件非常大】
商品 | 价格
飞机 | 1000
大炮 | 2000
迫击炮 | 1000
手枪 | 123
...
"""
# def read_content():
#     per_page_amount = 3
#     f = open('goods_list.txt', mode='r', encoding='utf-8')
#     count = 0
#     for i in f:
#         count += 1
#     f.close()
#     u, v = divmod(count, per_page_amount)
#     u = u + 1 if v else u
#     while True:
#         li = []
#         num = input('please enter a pages(1-%s): ' % u)
#         if num.upper() == 'N':
#             return
#         if not num.isdecimal():
#             print('输入不合法')
#             continue
#
#         if not 0 < int(num) <= u:
#             print('输入不合法')
#             continue
#
#         last_pages = (int(num)-1) * (per_page_amount)
#         index = 0
#         with open('goods_list.txt', mode='r', encoding='utf-8') as f:
#             for i in f:
#                 index += 1
#                 if last_pages < index <= last_pages + per_page_amount:
#                     li.append(i.strip())
#                     continue
#             c = 1
#             for i in li:
#                 print(c, i)
#                 c += 1
#
# read_content()

"""
7.程序设计：购物车
"""

"""
有如下商品列表 GOODS_LIST，用户可以选择进行购买商品并加入到购物车 SHOPPING_CAR 
中且可以选择要购买数量，购买完成之后将购买的所有商品写入到文件中【文件格式为：年_月_日.txt】。

注意：重复购买同一件商品时，只更改购物车中的数量。
"""
# 购物车
SHOPPING_CAR = {}

# 商品列表
GOODS_LIST = [
    {'id': 1, 'title': '飞机', 'price': 1000},
    {'id': 3, 'title': '大炮', 'price': 1000},
    {'id': 8, 'title': '迫击炮', 'price': 1000},
    {'id': 9, 'title': '手枪', 'price': 1000},
]


# # 购物车
# SHOPPING_CAR = {}
#
# # 商品列表
# GOODS_LIST = [
#     {'id': 1, 'title': '飞机', 'price': 1000},
#     {'id': 3, 'title': '大炮', 'price': 1000},
#     {'id': 8, 'title': '迫击炮', 'price': 1000},
#     {'id': 9, 'title': '手枪', 'price': 1000},
# ]
# from datetime import datetime
#
# def buy_goods():
#     # li 把商品的id存放到li中
#     li = []
#     for i in range(len(GOODS_LIST)):
#         print(GOODS_LIST[i]['id'], GOODS_LIST[i]['title'], GOODS_LIST[i]['price'])
#         li.append(str(GOODS_LIST[i]['id']))
#     # 把指定商品加入购物车
#
#     while True:
#         num = input('请输入要购买商品的id(N/n)：')
#         if num.upper() == 'N':
#             break
#         if num not in li:
#             print('输入不合法')
#             continue
#
#         for j in range(len(GOODS_LIST)):
#             if GOODS_LIST[j]['id'] == int(num):
#                 name = str(GOODS_LIST[j]['title'])
#         while True:
#             count = input('请输入购买数量：')
#             if not count.isdecimal():
#                 continue
#             count = int(count)
#             break
#         if SHOPPING_CAR.get(name):
#             SHOPPING_CAR[name] = SHOPPING_CAR[name] + count
#         else:
#             SHOPPING_CAR[name] = count
#
#     v1 = datetime.now()
#     y, m, d = v1.strftime('%Y/%m/%d').split('/')
#     file_name = '%s年%s月%s日.txt' % (y, m, d)
#     f = open(file_name, mode='a+', encoding='utf-8')
#     for i in SHOPPING_CAR:
#         content = i + ',' + str(SHOPPING_CAR[i]) + '\n'
#         f.write(content)
#         f.flush()
#     f.close()
#
#
# buy_goods()


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
        2019-11-11-09-59
            飞机|1000|10个
            大炮|2000|3个
        2019-11-12-11-56.txt
            迫击炮|10000|10个
            手枪|123|3个

    5.用户未登录的情况下，如果访问 商品流程 、我的购物车 时，提示登录之后才能访问，让用户先去选择登录（装饰器实现）。
"""







"""
9.请使用第三方模块xlrd读取一个excel文件中的内容。【课外】
"""
# import xlrd
#
# data = xlrd.open_workbook('example.xlsx') # 打开xls文件
# table = data.sheets()[0] # 打开第一张表
# nrows = table.nrows      # 获取表的行数
# for i in range(nrows):   # 循环逐行打印
#     if i == 0: # 跳过第一行
#         continue
#     print (table.row_values(i)) # 取前十三列














