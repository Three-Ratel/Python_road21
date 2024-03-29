"""
app 端获取幼教内容、绑定玩具信息二维码、语音聊天记录信息
content_list: 从服务器获取内容
get_cover: 获取歌曲图片
get_music: 获取歌曲
get_qr: 获取二维码
get_chat：获取聊天语音
"""
import os

from flask import Blueprint, jsonify, send_file

from config import mongo, RET, COVER_PATH, MUSIC_PATH, QRCODE_PATH, CHAT_PATH
from tools.redis_msg import get_msg_count

content = Blueprint('content', __name__)


@content.route('/content_list', methods=['post'])
def content_list():
    data_list = list(mongo.content.find({}))
    for index, info in enumerate(data_list):
        info['_id'] = str(info['_id'])
    RET['CODE'] = 0
    RET['MSG'] = '资源获取成功'
    RET['data'] = data_list

    return jsonify(RET)


@content.route('/get_cover/<filename>', methods=['get'])
def get_cover(filename):
    path_cover = os.path.join(COVER_PATH, filename)
    return send_file(path_cover)


@content.route('/get_music/<filename>', methods=['get'])
def get_music(filename):
    path_music = os.path.join(MUSIC_PATH, filename)
    return send_file(path_music)


@content.route('/get_qr/<filename>', methods=['get'])
def get_qr(filename):
    path_code = os.path.join(QRCODE_PATH, filename)
    return send_file(path_code)


@content.route('/get_chat/<filename>', methods=['get'])
def get_chat(filename):
    path_chat = os.path.join(CHAT_PATH, filename)
    return send_file(path_chat)


@content.route('/get_msg_num/<user_id>', methods=['post'])
def get_msg_num(user_id):
    return get_msg_count(user_id)
