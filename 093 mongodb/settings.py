"""mongodb设置"""
from pymongo import MongoClient

MC = MongoClient('127.0.0.1', 27017)
mongo = MC['game']

"""flask配置文件"""


class DebugConfig(object):
    DEBUG = True
