#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import logging
#
# logger = logging.getLogger()
# fh = logging.FileHandler('a.log')
# sh = logging.StreamHandler()
# fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
# sh.setFormatter(fmt)
# fh.setFormatter(fmt)
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# logger.warning('message')


# import logging
# # 对象1：文件 + 格式
# file_handler = logging.FileHandler('xxxxx.log', 'a', encoding='utf-8')
# fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
# file_handler.setFormatter(fmt)
#
# # 对象2：写（封装了对象1 ）
# logger = logging.Logger('xxx(在log中会显示)', level=logging.ERROR)
# logger.addHandler(file_handler)
#
# logger.error('你好')


"""
test
"""
# import logging
#
# logger = logging.getLogger()
# fh = logging.FileHandler('test.log')
# sh = logging.StreamHandler()
# # asctime:日志写入时间， name：logger对象名称， levelname：日志级别， module：模块名称
# fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s')
# sh.setFormatter(fmt)
# fh.setFormatter(fmt)
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# logger.error('message')

import time
import logging
from logging import handlers
# file_handler = logging.FileHandler('test.log', mode='a', encoding='utf-8')
# file_handler1 = logging.StreamHandler()
file_handler = handlers.TimedRotatingFileHandler('test.log', when='s', interval=1, encoding='utf-8')

logging.basicConfig(
    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[file_handler, ],
    level=logging.ERROR
)

for i in range(10):
    time.sleep(1)
    logging.error('message')
