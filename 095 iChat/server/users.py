from flask import Blueprint, request

from settings import RET
from settings import mongo

user = Blueprint('user', __name__)


@user.route('/register', methods=['post'])
def register():
    # print('注册')
    user_info = request.form.to_dict()
    print(user_info)
    user = mongo.users.find_one({'username': user_info.get('username')})
    if list(user):
        RET['code'] = -1
        RET['msg'] = '用户名已存在'
        RET['data'] = []
        return RET
    mongo.users.insert_one(user_info)
    RET['code'] = 0
    RET['msg'] = '注册成功'
    RET['data'] = []
    return RET


@user.route('/login', methods=['post'])
def login():
    user_info = request.form.to_dict()
    user_dict = mongo.users.find_one(user_info)
    print(type(user_dict))
    user_dict['_id'] = str(user_dict['_id'])
    user_dict.pop('password')
    RET['code'] = 0
    RET['msg'] = '登录成功'
    RET['data'] = user_dict
    # print(RET)
    return RET
