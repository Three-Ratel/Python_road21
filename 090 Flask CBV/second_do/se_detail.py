from flask import Blueprint, render_template, views, request
from second_do.se_settings import  STUDENT_DICT
info = Blueprint('detail', 'detail')


class Detail(views.MethodView):

    def get(self):
        sid = request.args.get('sid')
        if sid:
            flag = {'flag': 0}
            stus = {sid: STUDENT_DICT[int(sid)]}
        else:
            flag = {'flag': 1}
            stus = STUDENT_DICT
        return render_template('detail.html', stus=stus, flag=flag)


info.add_url_rule('/detail', view_func=Detail.as_view(name='detail'))
