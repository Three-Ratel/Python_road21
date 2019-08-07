from flask import Blueprint, views, render_template, redirect, request, session


log = Blueprint('log', 'login')


class Login(views.MethodView):

    def get(self, *args, **kwargs):
        return render_template('login.html')

    def post(self, *args, **kwargs):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'henry' and password == '123':
            session['username'] = username
            return redirect('/detail')


log.add_url_rule('/login', view_func=Login.as_view(name='login'))
