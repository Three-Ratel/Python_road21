from flask import Blueprint, request, jsonify

from config import mongo

chat = Blueprint('chat', __name__)


@chat.route('/recv_msg', methods=['post'])
def recv_msg():
    from_user = request.form.get('from_user')
    chat_info = mongo.chats.find_one({'user_list': {'$all': [from_user]}})

    if chat_info:
        ret = chat_info.get('chat_list')[-1:]
    else:
        ret = [{'from_user': '', 'to_user': '', 'chat': 'nomessage.mp3', 'createTime': ''}]
    print(ret)
    return jsonify(ret)


