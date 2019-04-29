#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
日志的本质：实例化3个对象
"""
import logging
# 对象1：文件 + 格式
file_handler = logging.FileHandler('xxxxx', 'a', encoding='utf-8')
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
file_handler.setFormatter(fmt)

# 对象2：写（封装了对象1 ）
logger = logging.Logger('xxx(在log中会显示)', level=logging.ERROR)
logger.addHandler(file_handler)

logger.error('你好')

"""
way1
"""
# import logging
# # logging.Error 默认级别
# logging.basicConfig(filename='cmdb.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=logging.WARNING)
#
# logging.log(10, '日志内容')  # 不写
# logging.debug('asdfgh')
# logging.log(30, 'asdfgh')  # 写
# logging.warning('asdfgh')


"""
way2: 推荐使用
"""
# import logging
#
# file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
# file_handler1 = logging.FileHandler(filename='x.log', mode='a', encoding='utf-8',)
# logging.basicConfig(
#
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',  # %p 用十六进制数格式化变量的地址, %a 表示星期
#     handlers=[file_handler, file_handler1, ],
#     level=logging.ERROR
# )
#
# logging.error('你好')

"""
way3：日志分割
模块：logging, logging.handlers,
"""
# import time
# import logging
# from logging import handlers
#
# # file_handler = logging.FileHandler(filename='split', mode='a', encoding='utf-8')
# file_handler = handlers.TimedRotatingFileHandler(filename='x3.log', when='s', interval=3, encoding='utf-8')
#
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H-%M-%S %p',
#     handlers=[file_handler, ],
#     level=logging.ERROR
#
# )
#
# for i in range(1, 10):
#     time.sleep(1)
#     logging.error('hello')

"""
示例：在应用日志时，如果想要保留异常的堆栈信息。
"""
# import logging
# import requests
#
# logging.basicConfig(
#     filename='wf.log',
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=logging.ERROR
# )
#
# try:
#     requests.get('http://www.xxx.com')
# except Exception as e:
#     msg = str(e) # 调用e.__str__方法
#     logging.error('你好', exc_info=True)   # 保留堆栈信息

