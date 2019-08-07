from flask import Flask, url_for, session, redirect, request
from flask_session import Session

from second_do.se_detail import info
from second_do.se_login import log
from second_do.se_settings import DebugConfig, EXEMPT_SET

app = Flask(__name__)
app.register_blueprint(log)
app.register_blueprint(info)
app.config.from_object(DebugConfig)
Session(app)


@app.template_global()
def query(name, sid=None):
    return f'{url_for(name)}?sid={sid}'


@app.before_request
def auth():
    if request.path in EXEMPT_SET:
        return

    elif session.get('username'):
        return

    return redirect('/login')


if __name__ == '__main__':
    app.run('127.0.0.1', 9527)
