from bson import ObjectId
from flask import Blueprint, request, jsonify

from config import mongo, RET

contact = Blueprint('contact', __name__)


@contact.route('/add_req', methods=['post'])
def add_req():
    request_info = request.form.to_dict()
    print(request_info)
    # 创建chatwindow
    chat = mongo.chats.insert_one({'user_list': [], 'chat_list': []})
    chat_id = str(chat.inserted_id)
    # 请求方的id
    req_id = request_info.get('toy_id')
    add_id = request_info.get('add_user')
    # 查找请求和添加方对象
    add_user = mongo.toys.find_one({'_id': ObjectId(add_id)})
    req_user = mongo.toys.find_one({'_id': ObjectId(req_id)})

    # 添加方
    add_user_info = {
        "friend_id": request_info.get('toy_id'),
        "friend_nick": req_user.get('baby_name'),
        "friend_remark": req_user.get('toy_name'),
        "friend_avatar": req_user.get('avatar'),
        "friend_chat": chat_id,
        "friend_type": "toy"
    }

    # add_user['friend_list'].append(add_user_info)
    # mongo.toys.update({'_id': ObjectId(add_id)}, {'$set': {'friend_list': add_user['friend_list']}})

    # 被添加方
    req_user_info = {
        "friend_id": request_info.get('add_user'),
        "friend_nick": add_user.get('baby_name'),
        "friend_remark": add_user.get('toy_name'),
        "friend_avatar": add_user.get('avatar'),
        "friend_chat": chat_id,
        "friend_type": "toy"
    }
    # req_user['friend_list'].append(req_user_info)
    # mongo.toys.update({'_id': ObjectId(req_id)}, {'$set': {'friend_list': req_user['friend_list']}})

    # print(add_user_info)
    # print(req_user_info)

    RET['CODE'] = 0
    RET['MSG'] = '添加好友请求成功'
    RET['DATA'] = {}

    return jsonify(RET)
