import os
from uuid import uuid4

from flask import Blueprint, request, render_template, send_file, redirect, session

from settings import mongo, ICON_PATH

user = Blueprint('user', __name__)


@user.route('/register', methods=['get', 'post'])
def register():
    if request.method == 'GET':
        return render_template('reg.html')

    user_info = request.form.to_dict()
    username = user_info.get('username')
    user = mongo.users.find_one({'username': username})
    if user:
        return render_template('reg.html', msg='用户名太火了，被被人抢注了')
    icon_file = request.files.get('icon')
    if icon_file:
        icon_name = f'{uuid4()}{icon_file.filename}'
        icon_file.save(os.path.join(ICON_PATH, icon_name))
        user_info['icon_name'] = icon_name
    else:
        user_info['icon_name'] = 'icon.jpg'

    # if username == 'test':
    #     return {'code': 200, 'msg': '注册成功'}

    user_info.pop('re_password')
    mongo.users.insert_one(user_info)

    return redirect('/login')


@user.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_info = request.form.to_dict()
        user = mongo.users.find_one(user_info)
        if user:
            user_id = str(user.get('_id'))
            session['user_id'] = user_id
            session['user_name'] = user.get('username')
            session['user_icon'] = user.get('icon_name')
            return redirect(f'/web_chat/{user_id}')
        return render_template('login.html', msg='用户名或密码错误')


@user.route('/get_icon/<filename>')
def get_icon(filename):
    return send_file(f"./icon/{filename}")
