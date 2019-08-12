from flask import Blueprint, request, render_template, views
from hm_settings import STUDENT_DICT

info = Blueprint('detail', __name__, url_prefix='')

"""CBV"""


class Detail(views.MethodView):

    def get(self, *args, **kwargs):
        sid = request.args.get('sid')
        if sid:
            stus = {sid: STUDENT_DICT[int(sid)]}
            flag = {'flag': 0}
            return render_template('detail.html', stus=stus, flag=flag, )
        flag = {'flag': 1}
        return render_template('detail.html', stus=STUDENT_DICT, flag=flag, )


info.add_url_rule('/detail', view_func=Detail.as_view(name='detail'))


"""FBV"""
@info.route('/detail', endpoint='detail')
def detail():
    sid = request.args.get('sid')
    if sid:
        stus = {sid: STUDENT_DICT[int(sid)]}
        flag = {'flag': 0}
        return render_template('detail.html', stus=stus, flag=flag, )
    flag = {'flag': 1}
    return render_template('detail.html', stus=STUDENT_DICT, flag=flag, )
