import hashlib
import time
from redis import Redis


class DebugConfig(object):
    DEBUG = True
    SECRET_KEY = 'ajdsfh^&%^*()nbnfdbsauy$%^&*(iyfxcvHSBNMN'
    JSONIFY_MIMETYPE = 'xixixi'
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = 'i am debug session'
    # 使用 redis
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis('127.0.0.1', 6379, db=2)


class TestConfig(object):
    TESTING = True
    t = time.time()
    SECRET_KEY = hashlib.md5(
        f'{t}ajdsfh^&%^*()nbnfdbsauy$%^&*(iyt&^%^ERdfxcvHSBNMN{t}'.encode('utf8')).hexdigest()
    JSONIFY_MIMETYPE = 'hahaha'
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = 'i am testing session'
    # 使用 redis
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis('127.0.0.1', 6379, db=2)


STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}

EXEMPT_SET = {
    '/login',
    '/static/style.css',
    '/static/jquery-1.10.2.js',
    '/static/vector.js',

}
