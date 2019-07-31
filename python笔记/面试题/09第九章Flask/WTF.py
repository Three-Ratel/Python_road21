from flask import Flask,request,render_template,g
from wtforms.fields import simple,core
from wtforms import Form, validators, widgets

app = Flask(__name__)
app.config["DEBUG"] = True

class LoginForm(Form):
    username = simple.StringField(
        label="用户名:",
        widget=widgets.TextInput(),
        validators=[
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(min=4,max=10,message="用户名不能小于%(min)d,不能大于%(max)d")
        ], # 声明校验方式
        id="username",
        #widget=widgets.FileInput(),
        render_kw={"class":"my_class"},
    )

    password = simple.PasswordField(
        label="密码:",
        validators=[
            validators.Length(max=10,min=6,message="password不能小于%(min)d,不能大于%(max)d"),
            validators.Regexp("\d+",message="密码只能是数字")
        ],
        id="pwd",
        render_kw={"style":"width:300px;"}
    )

    sub = simple.SubmitField(
        label="登陆",
        render_kw={"class": "bs"}
    )


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        lf = LoginForm()
        return render_template("login.html", lf=lf)
    else:
        new_lf = LoginForm(formdata=request.form)
        if new_lf.validate():
            g.username = request.form.get('username')
            return g.username
        else:
            return render_template("login.html", lf=new_lf)

class RegForm(Form):
    username = simple.StringField(
        label="用户名:",
        validators = [
            validators.Length(min=4,max=10,message="用户名不能小于%(min)d,不能大于%(max)d")
        ]
    )

    password = simple.PasswordField(
        label="密码:",
        validators=[
            validators.Length(max=10, min=6, message="password不能小于%(min)d,不能大于%(max)d")
        ]
    )

    repassword = simple.PasswordField(
        label="确认眼神:",
        validators = [
            validators.EqualTo("password",message="眼神未确认")
        ]
    )
    email = simple.StringField(
        label="邮箱",
        validators=[
            validators.Email(message="邮箱格式不符")
        ]
    )

    gender = core.RadioField(
        label="性别:",
        choices=[
            (1,"女"),
            (2,"男")
        ],
        coerce = int
    )

    hobby = core.SelectMultipleField(
        label="嗜好",
        choices=[
            (1,"小姐姐"),
            (2,"小萝莉"),
            (3,"小正太"),
            (4,"小哥哥")
        ],
        coerce = int
    )

    sub = simple.SubmitField(
        label="登陆",
        render_kw={"class": "bs"}
    )


@app.route("/reg",methods=["GET","POST"])
def reg():
    if request.method=="GET":
        regf = RegForm()
        return render_template("reg.html", regf=regf)

    else:
        new_regf = RegForm(formdata=request.form)
        if new_regf.validate():
            print(new_regf.data.get("gender"))
            print(new_regf.data.get("hobby"))
            return new_regf.data.get("username")
        else:
            return render_template("reg.html", regf=new_regf)

if __name__ == '__main__':
    app.run()
