from flask import Flask, request, render_template, send_file

app = Flask(__name__)
app.debug = True

from settings import mongo


@app.route('/login', methods=['get', 'post'])
def lgoin():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_info = request.form.to_dict()
        user = mongo.users.find(user_info)
        if user:
            return {'code': 200, 'msg': '登录成功'}
        return {'code': -1, 'msg': '登录失败'}


@app.route('/register', methods=['post'])
def register():
    user_info = request.form.to_dict()
    username = user_info.get('username')
    # print(username)
    user = mongo.users.find({'username': username})
    if list(user):
        return {'code': -1, 'msg': '用户名已存在'}
    if username.strip() != 'test':
        mongo.users.insert_one(user_info)
    return {'code': 200, 'msg': '注册成功'}


@app.route('/get_icon/<filename>')
def get_icon(filename):
    print(filename)
    return send_file(filename)


@app.route('/upload', methods=['post'])
def upload():
    # print(request.files)
    file = request.files.get('my_icon')
    file.save(file.filename)
    ret = {
        'code': 200,
        'http': "http://192.168.12.4:9527/get_icon/"+file.filename,
        'msg': '上传成功'
    }
    return ret


if __name__ == '__main__':
    app.run('0.0.0.0', 9527)
