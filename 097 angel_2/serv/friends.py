"""
friend_list: 获取好友列表
chat_list: 聊天信息
recv_msg: toy 获取消息
"""
import time
from uuid import uuid4
from bson import ObjectId
from flask import Blueprint, request, jsonify

from config import mongo, RET
from tools.BaiduAI import text2audio
from tools.redis_msg import get_msg

friend = Blueprint('friend', __name__)


@friend.route('/friend_list', methods=['post'])
def friend_list():
    user = request.form.to_dict()
    friend_info = mongo.users.find_one({'_id': ObjectId(user.get('_id'))})

    RET['CODE'] = 0
    RET['MSG'] = '好友查询'
    RET['DATA'] = friend_info.get('friend_list')
    print(RET)
    return jsonify(RET)


@friend.route('/chat_list', methods=['post'])
def chat_list():
    chat_info = request.form.to_dict()
    chat_id = chat_info.get('chat_id')
    chat_win = mongo.chats.find_one({'_id': ObjectId(chat_id)})

    RET['CODE'] = 0
    RET['MSG'] = '查询聊天记录'
    chat_list = chat_win.get('chat_list')
    if len(chat_list) >= 5:
        RET['DATA'] = chat_list[-5:]
    else:
        RET['DATA'] = chat_list

    return jsonify(RET)


@friend.route('/recv_msg', methods=['post'])
def recv_msg():
    from_user = request.form.get('from_user')
    to_user = request.form.get('to_user')
    chat_info = mongo.chats.find_one({'user_list': {'$all': [from_user, to_user]}})

    # 从玩具表中查找 friend_remark 即在 friend_list 中的备注
    toy = mongo.toys.find_one({'_id': ObjectId(to_user)})
    friend_list = toy.get('friend_list')
    friend_remark = '小伙伴'
    for friend in friend_list:
        if friend.get('friend_id') == from_user:
            friend_remark = friend.get('friend_remark')
            break

    # 从redis数据库中获取 未读条数
    count = get_msg(from_user, to_user)
    file_name = text2audio(f'您收到了来自{friend_remark}的{count}条消息', filename=f'{uuid4()}.mp3')
    if count != 0:
        ret = chat_info.get('chat_list')[-count:]
        ret.reverse()
        ret.append({"from_user": from_user, "chat": file_name, "create_time": time.time()})
    else:
        ret = [{"from_user": from_user, "chat": file_name, "create_time": time.time()}]
    return jsonify(ret)
