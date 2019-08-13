from flask import Flask, session

from users import user_bp
from play import play_bp
from settings import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)
app.register_blueprint(user_bp)
app.register_blueprint(play_bp)
app.secret_key = 'auhdhasjig28736t34654#$@^%&*(SJKALFMJKZBVIUFQ''lqJHGADJ'

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
