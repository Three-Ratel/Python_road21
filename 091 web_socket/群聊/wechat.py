from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket, WebSocketError

app = Flask(__name__)

ws_li = []
dead_li = []


@app.route('/chat')
def chat():
    # print(request.environ)
    ws = request.environ.get('wsgi.websocket')  # type:WebSocket
    ws_li.append(ws)
    while True:
        try:
            print('receive here')
            msg = ws.receive()
        except WebSocketError:
            if ws in ws_li:
                if ws_li:
                    ws = ws_li[0]
                else: return
                dead_li.append(ws)

        print('ws_li的个数：', len(ws_li))
        for u in ws_li:
            if u == ws:
                continue
            try:
                print(msg, '*' * 8)
                if msg:
                    u.send(msg)
            except:
                dead_li.append(u)
                print('dead_li', len(dead_li))

        print('ws_li为', ws_li)
        print('dead_li的个数', len(dead_li), dead_li)
        import time
        time.sleep(3)
        for i in dead_li:
            ws_li.remove(i)
            dead_li.clear()


@app.route('/ws')
def ws():
    return render_template('wechat.html')


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
