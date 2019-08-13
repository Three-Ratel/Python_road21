from flask import Blueprint, render_template, session

from settings import mongo

play_bp = Blueprint('play', __name__)


@play_bp.route('/play', methods=['get', 'post'])
def play():
    """
    {'_id': ObjectId('5d516100bd3b4612a485cde3'),
     'Player': {
         'UserName': 'henry',
         'ATC': 20, 'DEF': 20,
         'LIFE': 300, 'Equip': [],
         'Package': [
             {
                 'name': '大砍刀',
                 'atc': 20,
                 'def': -5,
                 'life': 0
             },
             {
                 'name': '黄金甲',
                 'atc': -5,
                 'def': 20,
                 'life': 200
             },
             {
                 'name': '小红药',
                 'atc': 5,
                 'def': 0,
                 'life': 100UserName
             }
         ]}}
    """
    username = session.get('username')
    player = mongo.players.find({'Player.UserName': 'henry'})
    enemy = mongo.players.find({'Player.UserName': {'$ne': username}})
    # print(list(player), list(enemy))
    for player in player:
        player = player.get('Player')
    # print(player, '----------player------------')
    enemy_list = []
    for enemy in enemy:
        one = enemy.get('Player')
        enemy_list.append(one)
    print(enemy_list, len(enemy_list), '----------enemy_list------------')
    return render_template('play.html', player=player, enemy=enemy_list)
