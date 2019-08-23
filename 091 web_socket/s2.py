import json

from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler  # 请求处理 WSGI HTTP
from geventwebsocket.server import WSGIServer  # 替换Flask原来的WSGI服务
from geventwebsocket.websocket import WebSocket  # 语法提示

app = Flask(__name__)

socket_dict = {}


@app.route("/ws/<username>")
def my_ws(username):
    # print(request.environ)
    ws_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    socket_dict[username] = ws_socket
    print(len(socket_dict), socket_dict)

    while True:
        print('----------------')
        try:
            try:
                msg = ws_socket.receive()
            except:
                socket_dict.pop(username)
                return

            print(msg)
            print('****************')
            if msg:
                msg_dict = json.loads(msg)
                receiver = msg_dict.get("receiver")
                receiver_socket = socket_dict.get(receiver)
                if receiver_socket:
                    receiver_socket.send(msg)

        finally:
            print(socket_dict, 'socket 连接')


@app.route("/wechat")
def wechat():
    return render_template("ws.html")


if __name__ == '__main__':
    http_serv = WSGIServer(("127.0.0.1", 5000), app,
                           handler_class=WebSocketHandler)  # handler_class=WSGIHandler / HTTPHandler
    http_serv.serve_forever()
