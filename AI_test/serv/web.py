import json
import os
from uuid import uuid4

from bson import ObjectId
from flask import Blueprint, render_template, send_file, request, jsonify

from serv.BaiduAI import dispose_reco
from settings import redis_cli, mongo, CHAT_PATH

web = Blueprint('web', __name__)


@web.route('/web_chat/<user_id>', methods=['get', 'post'])
def web_chat(user_id):
    friend_list = redis_cli.get('friend_list')
    if not friend_list:
        friend_list = []
    else:
        friend_list = json.loads(friend_list)
    user = mongo.users.find_one({'_id': ObjectId(user_id)})
    username = user.get('username')
    return render_template('web.html', user_id=user_id, username=username, friend_list=friend_list,
                           count=len(friend_list))


@web.route('/friend_list')
def friend_list():
    user_socket_dict = redis_cli.get('friend_list')
    return user_socket_dict


@web.route('/get_img/<img_name>')
def get_img(img_name):
    img_path = os.path.join('chat/img', img_name)
    return send_file(img_path)


@web.route('/web_uploader', methods=['post'])
def web_uploader():
    chat_info = request.form.to_dict()
    # 消息发送者和接收者以及语音信息
    sender = chat_info.get('user_id')
    receiver = chat_info.get('to_user')
    rec = request.files.get('reco')
    # 保存语音信息消息并进行格式转换为 mp3，录音格式为 .amr
    filename = f'{uuid4()}.mp3'

    file_path = os.path.join(CHAT_PATH, filename)
    rec.save(rec.filename)

    os.system(f'ffmpeg -i {rec.filename} {file_path}')
    os.remove(rec.filename)

    # 返回值
    RET = {}
    RET['CODE'] = 0
    RET['MSG'] = '上传成功'
    RET['data'] = {"filename": filename}
    # print(RET)
    return jsonify(RET)


@web.route('/get_chat/<filename>')
def get_chat(filename):
    filepath = os.path.join(CHAT_PATH, filename)
    return send_file(filepath)


@web.route('/ai_uploader', methods=['post'])
def ai_uploader():
    user_id = request.form.get('user_id')
    reco = request.files.get('reco')
    file_path = os.path.join(CHAT_PATH, reco.filename + '.wav')
    reco.save(file_path)

    ret = dispose_reco(user_id)

    return jsonify(ret)
