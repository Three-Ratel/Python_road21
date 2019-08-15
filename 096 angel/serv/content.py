import os

from flask import Blueprint, jsonify, send_file, request

from config import mongo, RET, COVER_PATH, MUSIC_PATH

content = Blueprint('content', __name__)


@content.route('/content_list', methods=['post'])
def content_list():
    data_list = list(mongo.content.find({}))
    for index, info in enumerate(data_list):
        info['_id'] = str(info['_id'])
    # print(data_list)
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
    # print(path_music)
    # os.system(f'ffplay {path_music}')
    return send_file(path_music)


@content.route('/scan_qr', methods=['post'])
def scan_qr():
    qrcode_dict = request.form.to_dict()
    device = mongo.devices.find_one(qrcode_dict)
    device_key = device['device_key']

    if not device:
        RET['CODE'] = 1
        RET['MSG'] = '请扫描玩具二维码'
        RET['DATA'] = {}
        return RET

    """用户扫描设备是我们的玩具，判断是否被用户绑定"""
    toy = mongo.toys.find_one({'device_key': device_key})
    # print(toy)
    if not toy:
        # 在toys表中没有查找到绑定设备
        RET['CODE'] = 0
        RET['MSG'] = '二维码扫描成功'
        RET['DATA'] = {
            "device_key": device_key
        }
    else:
        toy_id = str(device['_id'])
        RET['CODE'] = 2
        RET['MSG'] = '设备已经进行绑定'
        RET['DATA'] = {
            "toy_id": toy_id
        }
    return RET


@content.route('/bind_toy')
def bind_toy():
    pass
