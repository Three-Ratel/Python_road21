from flask import Flask
from serv.users import users
from serv.content import content
app = Flask(__name__)
app.debug = True
app.register_blueprint(users)
app.register_blueprint(content)



if __name__ == '__main__':
    app.run('0.0.0.0', 9527)
