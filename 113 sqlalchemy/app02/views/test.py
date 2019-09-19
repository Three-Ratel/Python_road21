from flask import Blueprint

from app02.models import Test, db

test = Blueprint('test', __name__)


@test.route('/exam/<name>')
def exam(name):
    print(name)
    t = Test(name=name)
    db.session.add(t)
    db.session.commit()
    return '200 OK'


@test.route('/res')
def res():
    res = Test.query.filter().all()
    print(res)
    return f'{len(res)}'
