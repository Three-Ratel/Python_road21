import json
from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)

websocket_dict = {}


@app.route('/chat/<username>')
def chat(username):
    socket_obj = request.environ.get('wsgi.websocket')  # type:WebSocket
    websocket_dict[username] = socket_obj
    print(socket_obj, username)

    while True:
        msg = socket_obj.receive()

        msg_dict = json.loads(msg)
        receiver = msg_dict.get('receiver')
        try:
            receiver_socket = websocket_dict.get(receiver)
            receiver_socket.send(msg)
        except:
            msg = {'sender': '系统',
                   'receiver': username,
                   'data': '对方不在线',
                   }
            socket_obj.send(json.dumps(msg))


@app.route('/ws')
def ws():
    return render_template('ptop.html')


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
    # app.run()
