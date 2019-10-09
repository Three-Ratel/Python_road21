#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
 题目
程序设计：新闻系统。（20分）
请自己设计合理的文件或数据结构，满足一下需求：

- 用户登录，需要让用户输入动态验证码 及 对密码进行md5加密。（4分）
- 新闻列表（无需登录）（4分）
  - 进入查看指定新闻详细（无需登录）（4分）
  - 对指定的新闻点赞（需登录，装饰器实现）（4分）
  - 对指定的新闻评论（需登录，装饰器实现）（4分）
"""

import hashlib

# 用户信息：示例密码是 123
USER_DICT = {'eric': '202cb962ac59075b964b07152d234b70', 'alex': '202cb962ac59075b964b07152d234b70'}

# 当前登录用户
CURRENT_USER = None

ARTICLE_LIST = [
    {
        'title': '震惊了，张思达居然...',
        'content': '张思达昨天在小区树下发现一条黑色的蛇，都冻僵了！他就把蛇揣到怀里面，想给它一点温暖。今天一大早他就在树上挂了个牌子:不准随地大小便',
        'comment': [
            {'data': '赞呀', 'user': '李鹏'},
            {'data': '是我干的', 'user': '李忠伟'},
        ],
        'up': 0,
    },
    {
        'title': '邵海鹏和他女朋友的故事',
        'content': '几个月前，女朋友跑了，几个月后，她回来了，怀着孕，流着泪说他不要她了，叫我陪她打掉孩子。我说生下来吧，我养。几个月后，孩子生下来了，我跑了！',
        'comment': [],
        'up': 0,
    },
    {
        'title': '世界上最苦命的人',
        'content': '一个乞丐上门行乞，我老婆见他可怜，给了他十块钱，又热情地端了一碗刚做好的饭菜给他吃。乞丐感动地接过了饭碗，狼吞虎咽地扒了两口，泪水忍不住流了下来：“谢谢你，大姐，遇见你以后才知道，原来我不是这个世界上最苦命的人，你老公才是。”',
        'comment': [],
        'up': 0,
    },
]


def encrypt_md5(arg):
    """
    md5加密
    :param arg:
    :return:
    """
    m = hashlib.md5()
    m.update(arg.encode('utf-8'))
    return m.hexdigest()


def register():
    """
    用户注册
    :return:
    """
    print('用户注册')
    while True:
        user = input('请输入用户名(N返回上一级)：')
        if user.upper() == 'N':
            return
        pwd = input('请输入密码：')
        if user in USER_DICT:
            print('用户已经存在，请重新输入。')
            continue
        USER_DICT[user] = encrypt_md5(pwd)
        print('%s 注册成功' % user)
        print(USER_DICT)


def login():
    """
    用户登录
    :return:
    """
    print('用户登录')
    while True:
        user = input('请输入用户名(N返回上一级)：')
        if user.upper() == 'N':
            return
        pwd = input('请输入密码：')
        if user not in USER_DICT:
            print('用户名不存在')
            continue

        encrypt_password = USER_DICT.get(user)
        if encrypt_md5(pwd) != encrypt_password:
            print('密码错误')
            continue

        print('登录成功')
        global CURRENT_USER
        CURRENT_USER = user
        return


def article_list():
    """
    文章列表
    :return:
    """
    while True:
        print('=================== 文章列表 ===================')
        for i in range(len(ARTICLE_LIST)):
            row = ARTICLE_LIST[i]
            msg = """%s.%s \n  赞(%s) 评论(%s)\n""" % (i + 1, row['title'], row['up'], len(row['comment']))
            print(msg)
        choice = input('请选择要查看的文章(N返回上一级)：')
        if choice.upper() == 'N':
            return
        choice = int(choice)
        choice_row_dict = ARTICLE_LIST[choice - 1]
        article_detail(choice_row_dict)


def article_detail(row_dict):
    """
    文章详细
    :param row_dict:
    :return:
    """
    show_article_detail(row_dict)
    func_dict = {'1': article_up, '2': article_comment}
    while True:
        print('1.赞；2.评论；')
        choice = input('请选择（N返回上一级）：')
        if choice.upper() == 'N':
            return
        func = func_dict.get(choice)
        if not func:
            print('选择错误，请重新输入。')
        result = func(row_dict)
        if result:
            show_article_detail(row_dict)
            continue

        print('用户未登录，请登录后再进行点赞和评论。')
        to_login = input('是否进行登录？yes/no：')
        if to_login == 'yes':
            login()


def show_article_detail(row_dict):
    print('=================== 文章详细 ===================')
    msg = '%s\n%s\n赞(%s) 评论(%s)' % (row_dict['title'], row_dict['content'], row_dict['up'], len(row_dict['comment']))
    print(msg)
    if len(row_dict['comment']):
        print('评论列表(%s)' % len(row_dict['comment']))
        for item in row_dict['comment']:
            comment = "    %s - %s" % (item['data'], item['user'])
            print(comment)


def auth(func):
    def inner(*args, **kwargs):
        if CURRENT_USER:
            return func(*args, **kwargs)
        return False

    return inner


@auth
def article_up(row_dict):
    """
    点赞文章
    :param row_dict:
    :return:
    """
    row_dict['up'] += 1
    print('点赞成功')
    return True


@auth
def article_comment(row_dict):
    """
    评论文章
    :param row_dict:
    :return:
    """
    while True:
        comment = input('请输入评论（N返回上一级）：')
        if comment.upper() == 'N':
            return True
        row_dict['comment'].append({'data': comment, 'user': CURRENT_USER})
        print('评论成功')


def run():
    """
    主函数
    :return:
    """
    print('=================== 系统首页 ===================')
    func_dict = {'1': register, '2': login, '3': article_list}
    while True:
        print('1.注册；2.登录；3.文章列表')
        choice = input('请选择序号：')
        if choice.upper() == 'N':
            return
        func = func_dict.get(choice)
        if not func:
            print('序号选择错误')
            continue
        func()


if __name__ == '__main__':
    run()
