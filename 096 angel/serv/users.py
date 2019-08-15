from flask import Blueprint, request, jsonify

from config import mongo, RET

users = Blueprint('users', __name__)


@users.route('/reg', methods=['post'])
def reg():
    user_info = request.form.to_dict()
    # print(user_info)
    mongo.users.insert_one(user_info)
    RET['CODE'] = 0
    RET['MSG'] = '注册成功'
    RET['DATA'] = {}
    return RET


@users.route('/login', methods=['post'])
def log():
    user_info = request.form.to_dict()
    # print(user_info)
    user = mongo.users.find_one(user_info, {'password': 0})
    user['_id'] = str(user['_id'])
    if list(user):
        RET['CODE'] = 0
        RET['MSG'] = '登录成功'
        RET['DATA'] = user
    else:
        RET['CODE'] = -1
        RET['MSG'] = '用户名或密码错误'
    # print(RET)
    return RET
