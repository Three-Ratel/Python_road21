from flask import Blueprint, request, session, render_template, redirect
from settings import mongo

user_bp = Blueprint('reg', __name__)


@user_bp.route('/reg', methods=['get', 'post'])
def reg():
    if request.method == 'GET':
        return render_template('reg.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_info = {'username': username, 'password':password}
        # print(username, list(mongo.users.find(user_info)))
        if not list(mongo.users.find({'username': username})):
            user = mongo.users.insert_one(user_info)
            player = mongo.players.insert_one({'Player':
                {
                    'UserName': username,
                    'ATC': 20,
                    'DEF': 20,
                    'LIFE': 300,
                    'Equip': [],
                    'Package': [
                        {'name': "大砍刀", 'atc': 20, 'def': -5, 'life': 0},
                        {'name': "黄金甲", 'atc': -5, 'def': 20, 'life': 200},
                        {'name': "小红药", 'atc': 5, 'def': 0, 'life': 100},
                    ]
                }})
            # print(user, player, '='*8)
        else:
            return '用户名已存在'
        return redirect('/login')


@user_bp.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user_info = request.form.to_dict()
        if mongo.users.find(user_info):
            session['username'] = user_info.get('username')
            return redirect('/play')
        return redirect('/login')