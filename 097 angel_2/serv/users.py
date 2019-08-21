"""
reg: 用户注册
login: 用户登录
auto_login: 登录过的用户自动登录
"""

from bson import ObjectId
from flask import Blueprint, request

from config import mongo, RET
from tools.redis_msg import get_msg_count

users = Blueprint('users', __name__)


@users.route('/reg', methods=['post'])
def reg():
    user_info = request.form.to_dict()
    user_info['avatar'] = 'baba.jpg' if user_info['gender'] == '2' else 'mama.jpg'
    user_info['bind_toys'] = []
    user_info['friend_list'] = []
    mongo.users.insert_one(user_info)
    RET['CODE'] = 0
    RET['MSG'] = '注册成功'
    RET['DATA'] = {}
    return RET


@users.route('/login', methods=['post'])
def login():
    user_info = request.form.to_dict()
    user = mongo.users.find_one(user_info, {'password': 0})
    user['_id'] = str(user['_id'])

    if user:
        RET['CODE'] = 0
        RET['MSG'] = '登录成功'
        RET['DATA'] = user
    else:
        RET['CODE'] = -1
        RET['MSG'] = '用户名或密码错误'
        RET['DATA'] = {}

    # 获取未读消息 数
    chat_dict = get_msg_count(str(user.get('_id')))

    RET['DATA']['chat'] = chat_dict

    # print(RET)
    return RET


@users.route('/auto_login', methods=['post'])
def auto_login():
    user_id = request.form.to_dict().get('_id')
    # print(user_id)
    user = mongo.users.find_one({'_id': ObjectId(user_id)}, {'password': 0})
    user['_id'] = str(user['_id'])

    RET['CODE'] = 0
    RET['MSG'] = '自动登录成功'
    RET['DATA'] = user

    # 获取未读消息 数
    chat_dict = get_msg_count(user_id)

    RET['DATA']['chat'] = chat_dict

    # print(RET)
    return RET
