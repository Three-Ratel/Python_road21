import json

from bson import ObjectId
from flask import Flask, request
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket
from redis import Redis

from settings import mongo

redis_cli = Redis(host='127.0.0.1', port=6379, db=6)

ws = Flask(__name__)
user_socket_dict = {}

friends = []


@ws.route('/chat/<user_id>')
def chat(user_id):
    user_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    if user_socket:
        user_socket_dict[user_id] = user_socket
    friend_list = list(user_socket_dict.keys())
    # print(friend_list, '好友id')
    friend_info = {}

    for i in friend_list:
        user = mongo.users.find_one({'_id': ObjectId(i)}, {'password': 0})
        friend_info['user_id'] = str(user.get('_id'))
        friend_info['user_name'] = user.get('username')
        friend_info['user_icon'] = user.get('icon_name')
        friends.append(friend_info.copy())
    # print('好友列表', friends)
    redis_cli.set('friend_list', json.dumps(friends))
    friends.clear()

    while True:
        try:
            msg = user_socket.receive()
        except:
            user_socket_dict.pop(user_id)
            redis_cli.set('friend_list', json.dumps(friends))
            return 'closed'

        if msg:
            msg_dict = json.loads(msg)
            receiver = msg_dict.get('receiver')  # type:str
            if receiver:
                receiver = receiver.strip('')
            sender = msg_dict.get('sender')
            if receiver:
                send_socket = user_socket_dict.get(receiver)
                msg_dict = json.dumps(msg_dict)
                try:
                    send_socket.send(msg_dict)
                except:
                    pass
            else:
                for user_id, ws_socket in user_socket_dict.items():
                    if user_id == sender:
                        continue
                    msg_dict = json.dumps(msg_dict)
                    try:
                        ws_socket.send(msg_dict)
                    except:
                        pass

        else:
            pass


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 9528), ws, handler_class=WebSocketHandler)
    http_server.serve_forever()
