#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from src import account
from src import article
from lib import logger

def run():
    """
    主函数
    :return:
    """
    print('=================== 系统首页 ===================')
    func_dict = {'1': account.register, '2': account.login, '3': article.article_list}
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

try:
    if __name__ == '__main__':
        run()

except Exception as e:
    logger.logger(e)

