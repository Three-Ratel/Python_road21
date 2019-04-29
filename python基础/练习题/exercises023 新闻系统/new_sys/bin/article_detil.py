#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os
    import sys
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_PATH)
    from bin import up
    from src import account
    from db import data
    from lib import logger

    def article_detail(row_dict):
        """
        文章详细
        :param row_dict:
        :return:
        """
        show_article_detail(row_dict)
        func_dict = {'1': up.article_up, '2': up.article_comment}
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
                account.login()


    def show_article_detail(row_dict):
        print('=================== 文章详细 ===================')
        msg = '%s\n%s\n赞(%s) 评论(%s)' % (row_dict['title'], row_dict['content'], row_dict['up'], len(row_dict['comment']))
        print(msg)
        if len(row_dict['comment']):
            print('评论列表(%s)' % len(row_dict['comment']))
            for item in row_dict['comment']:
                comment = "    %s - %s" % (item['data'], item['user'])
                print(comment)


    if __name__ == '__main__':
        article_detail()
        show_article_detail()
except Exception as e:
    logger.logger(e)

