"""
app_uploader: app 发送语音给玩具
toy_uploader: toy 给app回语音
"""
import os
import time
from uuid import uuid4

from bson import ObjectId
from flask import Blueprint, request, jsonify

from config import mongo, RET, CHAT_PATH
from tools.BaiduAI import text2audio, dispose_reco
from tools.redis_msg import set_msg

uploader = Blueprint('uploader', __name__)


@uploader.route('/app_uploader', methods=['post'])
def app_uploader():
    chat_info = request.form.to_dict()
    # print('chat_info', chat_info)
    # 消息发送者和接收者以及语音信息
    sender = chat_info.get('user_id')
    receiver = chat_info.get('to_user')
    rec = request.files.get('reco_file')

    # 保存语音信息消息并进行格式转换为 mp3，录音格式为 .amr
    file_path = os.path.join(CHAT_PATH, rec.filename)
    rec.save(file_path)
    os.system(f'ffmpeg -i {file_path} {file_path}.mp3')
    os.remove(file_path)

    # 需要更新的聊天记录
    rec_chat_info = {
        'from_user': sender,
        'to_user': receiver,
        'chat': f'{rec.filename}.mp3',
        'createTime': time.time()
    }

    # 更新聊天记录表中的 聊天记录
    mongo.chats.update_one({'user_list': {'$all': [sender, receiver]}}, {'$push': {'chat_list': rec_chat_info}})
    # 存储未读信息条数
    set_msg(sender, receiver)

    # 如果没有找到则使用默认值：小伙伴
    friend_remark = '小伙伴'
    friend_list = mongo.toys.find_one({'_id': ObjectId(receiver)}).get('friend_list')
    for i in friend_list:
        if i.get('friend_id') == sender:
            friend_remark = i.get('friend_remark')
            break

    # 使用 百度AI 合成消息提示音
    filename = text2audio(f'您收到了来自{friend_remark}的1条消息', filename=f'{uuid4()}.mp3')
    RET = {}
    # 返回值
    RET['CODE'] = 0
    RET['MSG'] = '上传成功'
    RET['DATA'] = {"filename": filename, "friend_type": "app"}
    print(RET)
    return jsonify(RET)


@uploader.route('/toy_uploader', methods=['post'])
def toy_uploader():
    chat_info = request.form.to_dict()

    # toy 发送的数据信息，发送者，接收者和语音
    sender = chat_info.get('user_id')
    receiver = chat_info.get('to_user')
    # print(chat_info)
    # 语音消息
    rec = request.files.get('reco')
    file_path = os.path.join(CHAT_PATH, rec.filename)
    rec.save(file_path)

    # 为toy的录音文件创建一个文件名 .mp3
    filename = f'{rec.filename}{uuid4()}.mp3'
    new_file_path = os.path.join(CHAT_PATH, filename)
    os.system(f'ffmpeg -i {file_path} {new_file_path}')
    os.remove(file_path)

    # 构造聊天记录并更新数据库
    rec_chat_info = {
        'from_user': sender,
        'to_user': receiver,
        'chat': f'{filename}',
        'createTime': time.time()
    }
    mongo.chats.update_one({'user_list': {'$all': [sender, receiver]}}, {'$push': {'chat_list': rec_chat_info}})
    # 存储未读信息条数
    set_msg(sender, receiver)

    # 返回值
    RET['CODE'] = 0
    RET['MSG'] = '上传成功'
    RET['DATA'] = {"filename": f"{filename}", "friend_type": "app"}
    # print('toy上传返回值', RET)
    return jsonify(RET)


@uploader.route('/ai_uploader', methods=['post'])
def ai_uploader():
    toy_id = request.form.get('toy_id')
    reco = request.files.get('reco')
    file_path = os.path.join(CHAT_PATH, reco.filename + '.wav')
    reco.save(file_path)

    ret = dispose_reco(toy_id)

    return jsonify(ret)
