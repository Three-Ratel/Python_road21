import os
import time
from uuid import uuid4

from bson import ObjectId
from flask import Blueprint, request, jsonify

from baiduAI import text2audio
from config import mongo, RET, CHAT_PATH

friend = Blueprint('friend', __name__)


@friend.route('/friend_list', methods=['post'])
def friend_list():
    user = request.form.to_dict()
    friend_info = mongo.users.find_one({'_id': ObjectId(user.get('_id'))})

    RET['CODE'] = 0
    RET['MSG'] = '好友查询'
    RET['DATA'] = friend_info.get('friend_list')
    return jsonify(RET)


@friend.route('/chat_list', methods=['post'])
def chat_list():
    chat_info = request.form.to_dict()
    chat_id = chat_info.get('chat_id')
    chat_win = mongo.chats.find_one({'_id': ObjectId(chat_id)})

    RET['CODE'] = 0
    RET['MSG'] = '查询聊天记录'
    RET['DATA'] = chat_win.get('chat_list')[-1:]

    return jsonify(RET)


@friend.route('/app_uploader', methods=['post'])
def app_uploader():
    chat_info = request.form.to_dict()
    print('chat_info', chat_info)
    sender = chat_info.get('user_id')
    receiver = chat_info.get('to_user')
    rec = request.files.get('reco_file')
    file_path = os.path.join(CHAT_PATH, rec.filename)
    rec.save(file_path)
    os.system(f'ffmpeg -i {file_path} {file_path}.mp3')
    os.remove(file_path)

    rec_chat_info = {
        'from_user': sender,
        'to_user': receiver,
        'chat': f'{rec.filename}.mp3',
        'createTime': time.time()

    }

    mongo.chats.update_one({'user_list': {'$all': [sender, receiver]}}, {'$push': {'chat_list': rec_chat_info}})

    print(mongo.chats.find_one({'user_list': {'$all': [sender, receiver]}}))
    friend_remark = '你爸爸'
    friend_list = mongo.toys.find_one({'_id': ObjectId(receiver)}).get('friend_list')
    for i in friend_list:
        if i.get('friend_id') == sender:
            friend_remark = i.get('friend_remark')
            break

    text2audio(f'你收到了来自{friend_remark}的消息')
    RET['CODE'] = 0
    RET['MSG'] = '上传成功'
    RET['DATA'] = {"filename": 'notification.mp3', "friend_type": "app"}
    return jsonify(RET)


@friend.route('/toy_uploader', methods=['post'])
def toy_uploader():
    chat_info = request.form.to_dict()
    sender = chat_info.get('user_id')
    receiver = chat_info.get('to_user')
    print(chat_info)
    # 语音消息
    rec = request.files.get('reco')
    file_path = os.path.join(CHAT_PATH, rec.filename)
    rec.save(file_path)

    # 为toy的录音文件创建一个文件名 .mp3
    uid = uuid4()
    filename = f'{rec.filename}{uid}.mp3'
    new_file_path = os.path.join(CHAT_PATH, filename)
    os.system(f'ffmpeg -i {file_path} {new_file_path}')
    print(file_path, new_file_path)
    os.remove(file_path)

    rec_chat_info = {
        'from_user': sender,
        'to_user': receiver,
        'chat': f'{filename}',
        'createTime': time.time()
    }
    mongo.chats.update_one({'user_list': {'$all': [sender, receiver]}}, {'$push': {'chat_list': rec_chat_info}})

    RET['CODE'] = 0
    RET['MSG'] = '上传成功'
    RET['DATA'] = {"filename": f"{filename}", "friend_type": "app"}
    print(RET)
    return jsonify(RET)
