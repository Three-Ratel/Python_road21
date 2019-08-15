import json
import os

from flask import Flask, request
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket

from settings import RECORD

ws_app = Flask(__name__)
user_socket_dict = {}


@ws_app.route('/chat/<user_id>')
def chat(user_id):
    user_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    if user_socket:
        user_socket_dict[user_id] = user_socket
    print(user_socket_dict)

    while True:
        msg = user_socket.receive()
        msg_dict = json.loads(msg)
        print(msg_dict)
        receiver = msg_dict.get('receiver')
        filename = msg_dict.get('data')
        send_socket = user_socket_dict.get(receiver)
        send_socket.send(filename)


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 9528), ws_app, handler_class=WebSocketHandler)
    http_server.serve_forever()
