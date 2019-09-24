from flask import Flask, send_file, session, redirect, jsonify, request, render_template

app = Flask(__name__, static_folder='img', static_url_path='/static')
# app.config['DEBUG'] = True
# app.secret_key = '!*%#&^$#$&&$##%FGHGjJdt(,"S<.dfg?./gdy{-@fhg?><'
# app.session_cookie_name = 'ah'
# app.permanent_session_lifetime = 10
# app.config['JSONIFY_MIMETYPE'] = 'sddd'
from settings import DebugConfig

app.config.from_object(DebugConfig)


# app.config.from_object(TestConfig)


def war(func):
    def inner(*args, **kwargs):
        # print(session.get('username'))
        if session.get('username'):
            return func(*args, **kwargs)
        return redirect('/login')

    return inner


@app.route('/test/<filename>', endpoint='test', strict_slashes=False, )
@war
def test(filename):
    return send_file(f'img/{filename}')


@app.route('/index/<count>_<ty>', endpoint='index', redirect_to='/')
@war
def index(count, ty):
    # print(count, type(count))
    # print(ty, type(ty))
    return f'you are visiting index!{count}'


@app.route('/')
@war
def home():
    # return 'Here is home page'
    # return render_template('test.html')
    return jsonify('ahh')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.form.get('username') == 'henry':
        session['username'] = True
        return redirect('/')
    return 'failed to login in!'


@app.route('/xxx')
def user():
    return 'I am in test!'


"""蓝图"""
from bp import bp
from stu import test

app.register_blueprint(bp)
app.register_blueprint(test)


if __name__ == '__main__':
    app.run()
