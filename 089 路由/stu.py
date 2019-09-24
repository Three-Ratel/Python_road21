from flask import Blueprint, request, render_template

test = Blueprint('test', __name__,)


@test.route('/stu')
def stu():
    return render_template('test.html')
