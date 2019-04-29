#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    import os
    import sys
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_PATH)
    from lib import auth
    from config import settings
    from lib import logger

    @auth.auth
    def article_up(row_dict):
        """
        点赞文章
        :param row_dict:
        :return:
        """
        row_dict['up'] += 1
        print('点赞成功')
        return True


    @auth.auth
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
            row_dict['comment'].append({'data': comment, 'user': settings.CURRENT_USER})
            print('评论成功')


    if __name__ == '__main__':
        article_up()
        article_comment()
except Exception as e:
    logger.logger(e)
