from flask import Flask, views, session
from flask_session import Session
from redis import Redis
from settings import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)

# app.secret_key = '$IHJHg823rhg$%^&*&)Gh(oi2dA:"<A:FAOIas5dfGF%45'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis('192.168.12.9', 6379, db=10)
Session(app)
app.session_interface



class Login(views.MethodView):

    def get(self, *args, **kwargs):
        return 'here is get'

    def post(self, *args, **kwargs):
        return 'here is post'


app.add_url_rule('/login', view_func=Login.as_view(name='m_login', ))


@app.route('/sets')
def sets():
    session['key'] = 'xihaha'
    return 'session was set'


@app.route('/gets')
def gets():
    session['key'] = 'xihaha'
    print(session.get('key'))
    return 'ok'


if __name__ == '__main__':
    app.run()
