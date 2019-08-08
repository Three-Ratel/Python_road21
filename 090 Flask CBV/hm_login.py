from flask import Blueprint, request, render_template, session, redirect, views

log = Blueprint('login', __name__, )

"""CBV"""


class Login(views.MethodView):

    def get(self, *args, **kwargs):
        return render_template('login.html')

    def post(self, *args, **kwargs):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'henry' and password == '123':
            session['username'] = 'henry'
            return redirect('/detail')
        return 'Failed'


log.add_url_rule('/login', view_func=Login.as_view(name='login'))


"""FBV"""
# @log.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username == 'henry' and password == '123':
#             session['username'] = 'henry'
#             return redirect('/detail')
#         return 'Failed'
