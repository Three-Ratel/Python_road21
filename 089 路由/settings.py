import hashlib
import time


class DebugConfig(object):
    DEBUG = True
    SECRET_KEY = 'ajdsfh^&%^*()nbnfdbsauy$%^&*(iyfxcvHSBNMN'
    JSONIFY_MIMETYPE = 'xixixi'
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = 'i am debug session'


class TestConfig(object):
    TESTING = True
    SECRET_KEY = hashlib.md5(
        f'{time.time()}ajdsfh^&%^*()nbnfdbsauy$%^&*(iyt&^%^ERdfxcvHSBNMN{time.time()}'.encode('utf8')).hexdigest()
    JSONIFY_MIMETYPE = 'hahaha'
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_COOKIE_NAME = 'i am testing session'


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
