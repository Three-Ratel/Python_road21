"""
要求:
1.登录页面
2.学生概况页面 ID name 点击详情
3.学生详情页面 ID name age gender
"""

from flask import Flask, session, redirect, request, url_for

from settings import EXEMPT_SET

app = Flask(__name__)
from settings import DebugConfig

app.config.from_object(DebugConfig)
# app.config.from_object(TestConfig)

from login import log
from detail import info

app.register_blueprint(log)
app.register_blueprint(info)


@app.before_request
def auth():
    # print(request.path, )
    if request.path in EXEMPT_SET:
        return
    if not session.get('username'):
        return redirect('/login')


# @app.errorhandler(404)
# def error404(error):
#     # print(error)
#     return redirect('/detail')

@app.template_global()
def query(name, sid):
    # print(url_for(name))
    # print(f'{url_for(name)}?sid={sid}')
    return f'{name}?sid={sid}'


if __name__ == '__main__':
    app.run()
    # app.__call__()
