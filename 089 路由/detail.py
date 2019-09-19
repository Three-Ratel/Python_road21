from flask import Blueprint, request, render_template

from settings import STUDENT_DICT

# info = Blueprint('detail', __name__, url_prefix='/xx')
info = Blueprint('detail', __name__)


@info.route('/detail', endpoint='detail')
def detail():
    print(request.url)
    sid = request.args.get('sid')
    if sid:
        stus = {sid: STUDENT_DICT[int(sid)]}
        flag = {'flag': 0}
        return render_template('exec/detail.html', stus=stus, flag=flag, )
    flag = {'flag': 1}
    return render_template('exec/detail.html', stus=STUDENT_DICT, flag=flag, )
