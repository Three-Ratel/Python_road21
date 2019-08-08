from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket
import json

app = Flask(__name__)

websocket_dict = {}


@app.route('/chat/<username>')
def chat(username):
    # print(request.environ)
    websocket_obj = request.environ.get('wsgi.websocket')  # type:WebSocket
    websocket_dict[username] = websocket_obj

    while True:
        msg = websocket_obj.receive()

        msg_dict = json.loads(msg)
        receiver = msg_dict.get('receiver')
        receiver_socket = websocket_dict.get(receiver)

        receiver_socket.send(msg)





@app.route('/ws')
def ws():
    return render_template('ptop.html')


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
