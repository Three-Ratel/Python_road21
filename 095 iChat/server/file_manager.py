import os

from flask import Blueprint, request, send_file

from settings import AVATAR, RECORD

fm = Blueprint('fm', __name__)


@fm.route('/upload', methods=['post'])
def upload():
    avatar = request.files.get('avatar')
    avatar_path = os.path.join(AVATAR, avatar.filename)
    avatar.save(avatar_path)
    ret = {
        'code': 0,
        'filename': avatar.filename,
    }
    # print(avatar_path)
    return ret


@fm.route('/upload_record', methods=['post'])
def upload_record():
    record = request.files.get('record')
    reco_path = os.path.join(RECORD, record.filename)
    record.save(reco_path)
    ret = {
        'code': 0,
        'filename': record.filename,
    }
    # print(avatar_path)
    return ret


@fm.route('/get_avatar/<filepath>')
def get_avatar(filepath):
    filepath = os.path.join(AVATAR, filepath)
    return send_file(filepath)


@fm.route('/get_chat/<filepath>')
def get_chat(filepath):
    filename = os.path.join(RECORD, filepath)
    os.system(f'ffmpeg -i {filename} {filename}.mp3')
    os.remove(filename)
    return send_file(f'{filename}.mp3')