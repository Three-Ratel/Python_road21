#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from db import data
from bin  import article_detil


def article_list():
    """
    文章列表
    :return:
    """
    while True:
        print('=================== 文章列表 ===================')
        for i in range(len(data.ARTICLE_LIST)):
            row = data.ARTICLE_LIST[i]
            msg = """%s.%s \n  赞(%s) 评论(%s)\n""" % (i + 1, row['title'], row['up'], len(row['comment']))
            print(msg)
        choice = input('请选择要查看的文章(N返回上一级)：')
        if choice.upper() == 'N':
            return
        choice = int(choice)
        choice_row_dict = data.ARTICLE_LIST[choice - 1]
        article_detil.article_detail(choice_row_dict)


if __name__ == '__main__':
    article_list()
