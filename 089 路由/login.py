from flask import Blueprint, request, render_template, session, redirect

log = Blueprint('login', __name__)


@log.route('/login', methods=['GET', 'POST'])
def login():
    print(request.path, )
    if request.method == 'GET':
        return render_template('exec/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'henry' and password == '123':
            session['username'] = 'henry'
            return redirect('/detail')
        return 'Failed'
