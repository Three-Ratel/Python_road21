from flask import Flask

from serv.users import user
from serv.web import web

app = Flask(__name__)
app.secret_key = 'aksdjhfhYFG%^^&*()GCvdkjanf;kldsh8firtyf'
app.debug = True

app.register_blueprint(user)
app.register_blueprint(web)

if __name__ == '__main__':
    app.run('0.0.0.0', 9527)
