from flask import session, Flask
from flask_session import Session
from redis import Redis
from flask import g

app = Flask(__name__)
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis("127.0.0.1",6379,db=15)  #指定session存放的数据库
Session(app)

@app.route("/login")
def login():
    session["key"] = "value"
    return "已经创建了session"

@app.route("/look")
def look():

    return session.get("key")




if __name__ == '__main__':
    app.run()
