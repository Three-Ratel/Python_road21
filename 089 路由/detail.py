from flask import Blueprint, request, render_template

from settings import STUDENT_DICT

info = Blueprint('detail', __name__)


def query(name, sid):
    return f'/{name}?sid={sid}'


@info.route('/detail')
def detail():
    sid = request.args.get('sid')
    if sid:
        stus = {sid: STUDENT_DICT[int(sid)]}
        flag = {'flag': 0}
        return render_template('exec/detail.html', stus=stus, flag=flag, query=query)
    flag = {'flag': 1}
    return render_template('exec/detail.html', stus=STUDENT_DICT, flag=flag, query=query)
