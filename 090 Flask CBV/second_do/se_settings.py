from redis import Redis


class DebugConfig(object):
    DEBUG = True
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='127.0.0.1', port=6379, db=1)


class TestConfig(DebugConfig):
    DEBUG = False
    TESTING = True


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