# 1. 登陆和注册

## 1.1 forms

- 自动生成前端标签

```python
# crm中的forms.py
import hashlib
from django import forms
from django.core.exceptions import ValidationError
from crm import models

class RegForm(forms.ModelForm):
  	# 由于类中没有re_password,需要进行手写（优先级高于自动生成）
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "您的密码", 'autocomplete': "off", }))
    re_password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "确认您的密码", 'autocomplete': "off", }))
    class Meta:
        model = models.UserProfile
        # __all__表示生成类中的所有字段, fields也支持[字段名1，字段名2...]
        fields = '__all__'
        # 表示排除某些字段
        exclude = ['is_active',]
        # 多个字段写在一起的插件
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': "您的用户名", 'autocomplete': "off", }),
            'name': forms.TextInput(attrs={'placeholder': "您的名字", 'autocomplete': "off", }),
            'mobile': forms.TextInput(attrs={'placeholder': "您的手机号", 'autocomplete': "off", }),}
        # 自定义错误信息
        error_messages = {
            'username': {
                'required': '信息不能为空',
                'invalid': '邮箱格式不正确',}}
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(self.cleaned_data.get('department'))
        if password == re_password:
            md = hashlib.md5(b'sajdfkh')
            md.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md.hexdigest()
            return self.cleaned_data
        
        # 把错误信息加载到，某个字段的错误中
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
```

## 1.2 html页面

### 1. 注册页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <title>注册</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<div class="register-container">
    <h1>Welcom to sign up Henry's CRM</h1>
    <div class="connect">
        <p>Link the world. Share to world.</p>
    </div>
    <form action="" method="post" id="registerForm" novalidate="novalidate">
        {% csrf_token %}
        <div>
            {{ form_obj.username }}
            {{ form_obj.username.errors.0 }}
        </div>
        <div>
            {{ form_obj.password }}
            {{ form_obj.password.errors.0 }}
        </div>
        <div>
            {{ form_obj.re_password }}
            {{ form_obj.re_password.errors.0 }}
        </div>
        <div>
            {{ form_obj.name }}
            {{ form_obj.name.errors.0 }}
        </div>
        <div>
            {{ form_obj.mobile }}
            {{ form_obj.mobile.errors.0 }}
        </div>
        <div>
            {{ form_obj.department}}
            {{ form_obj.department.errors.0 }}
        </div>
        <button id="submit" type="submit">注 册</button>
    </form>
    <a href="/crm/login">
        <button type="button" class="register-tis">已经有账号？</button>
    </a>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/common.js' %}"></script>
<script src="{% static 'js/supersized.3.2.7.min.js' %}"></script>
<script src="{% static 'js/supersized-init.js' %}"></script>
<script src="{% static 'js/jquery.validate.min.js' %}"></script>
</body>
</html>
```

### 2. 登陆页面

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <title>登陆</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<div class="login-container">
    <h1>Henry's CRM</h1>
    <div class="connect">
        <p>Link the world. Share to world.</p>
    </div>
    <form action="" method="post" id="loginForm" novalidate="novalidate">
        {% csrf_token %}
        <div>
            <input type="text" name="username" class="username" placeholder="用户名" autocomplete="off">
        </div>
        <div>
            <input type="password" name="password" class="password" placeholder="密码" oncontextmenu="return false"
                   onpaste="return false">
        </div>
        <div>
            {{ error }}
        </div>
        <button id="submit" type="submit">登 陆</button>
    </form>
    <a href="/crm/reg/">
        <button type="button" class="register-tis">还有没有账号？</button>
    </a>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/common.js' %}"></script>
<script src="{% static 'js/supersized.3.2.7.min.js' %}"></script>
<script src="{% static 'js/supersized-init.js' %}"></script>
<script src="{% static 'js/jquery.validate.min.js' %}"></script>
</body>
</html>
```

## 1.3 业务逻辑

```python
import hashlib
from django import forms
from django.core.exceptions import ValidationError
from crm import models

class RegForm(forms.ModelForm):
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "您的密码", 'autocomplete': "off", }))
    re_password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': "确认您的密码", 'autocomplete': "off", }))

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        exclude = ['is_active']
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': "您的用户名", 'autocomplete': "off", }),
            'name': forms.TextInput(attrs={'placeholder': "您的名字", 'autocomplete': "off", }),
            'mobile': forms.TextInput(attrs={'placeholder': "您的手机号", 'autocomplete': "off", }),}
        error_messages = {
            'username': {
                'required': '信息不能为空',
                'invalid': '邮箱格式不正确',}}

    def clean(self):
        # self._validate_unique = True
        super().clean()    # 校验邮箱名是否已经在数据库中
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md = hashlib.md5(b'sajdfkh')
            md.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md.hexdigest()
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')

```

### 1.4 models.py

- 数据表的创建

```python
from django.db import models
from multiselectfield import MultiSelectField

course_choices = (('Linux', 'Linux中高级'),
                  ('PythonFullStack', 'Python高级全栈开发'),)

class_type_choices = (('fulltime', '脱产班',),
                      ('online', '网络班'),
                      ('weekend', '周末班',),)

source_type = (('qq', "qq群"),
               ('referral', "内部转介绍"),
               ('website', "官方网站"),
               ('baidu_ads', "百度推广"),
               ('office_direct', "直接上门"),
               ('WoM', "口碑"),
               ('public_class', "公开课"),
               ('website_luffy', "路飞官网"),
               ('others', "其它"),)

enroll_status_choices = (('signed', "已报名"),
                         ('unregistered', "未报名"),
                         ('studying', '学习中'),
                         ('paid_in_full', "学费已交齐"))

seek_status_choices = (('A', '近期无报名计划'), ('B', '1个月内报名'), ('C', '2周内报名'), ('D', '1周内报名'),
                       ('E', '定金'), ('F', '到班'), ('G', '全款'), ('H', '无效'),)
pay_type_choices = (('deposit', "订金/报名费"),
                    ('tuition', "学费"),
                    ('transfer', "转班"),
                    ('dropout', "退学"),
                    ('refund', "退款"),)

attendance_choices = (('checked', "已签到"),
                      ('vacate', "请假"),
                      ('late', "迟到"),
                      ('absence', "缺勤"),
                      ('leave_early', "早退"),)

score_choices = ((100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (70, 'B-'), (60, 'C+'), (50, 'C'),(40, 'C-'), (0, ' D'), (-1, 'N/A'), (-100, 'COPY'), (-1000, 'FAIL'),)


class Department(models.Model):
    """
    部门表
    """
    name = models.CharField(max_length=32, verbose_name="部门名称")
    count = models.IntegerField(verbose_name="人数", default=0)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    用户表
    """
    username = models.EmailField(max_length=255, unique=True, )
    password = models.CharField(max_length=128)
    name = models.CharField('名字', max_length=32)
    department = models.ForeignKey('Department', default=None, blank=True, null=True)
    mobile = models.CharField('手机', max_length=32, default=None, blank=True, null=True)
    memo = models.TextField('备注', blank=True, null=True, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    客户表
    """
    qq = models.CharField('QQ', max_length=64, unique=True, help_text='QQ号必须唯一')
    qq_name = models.CharField('QQ昵称', max_length=64, blank=True, null=True)
    name = models.CharField('姓名', max_length=32, blank=True, null=True, help_text='学员报名后，请改为真实姓名')
    sex_type = (('male', '男'), ('female', '女'))
    sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
    birthday = models.DateField('出生日期', default=None, help_text="格式yyyy-mm-dd", blank=True, null=True)
    phone = models.BigIntegerField('手机号', blank=True, null=True)
    source = models.CharField('客户来源', max_length=64, choices=source_type, default='qq')
    introduce_from = models.ForeignKey('self', verbose_name="转介绍自学员", blank=True, null=True)
    course = MultiSelectField("咨询课程", choices=course_choices)
    class_type = models.CharField("班级类型", max_length=64, choices=class_type_choices, default='fulltime')
    customer_note = models.TextField("客户备注", blank=True, null=True, )
    status = models.CharField("状态", choices=enroll_status_choices, max_length=64, default="unregistered",
                              help_text="选择客户此时的状态")
    last_consult_date = models.DateField("最后跟进日期", auto_now_add=True)
    next_date = models.DateField("预计再次跟进时间", blank=True, null=True)
    consultant = models.ForeignKey('UserProfile', verbose_name="销售", related_name='customers', blank=True, null=True, )
    class_list = models.ManyToManyField('ClassList', verbose_name="已报班级", )

    def __str__(self):
        if self.name:
            return self.name
        return 'None'


class Campus(models.Model):
    """
    校区表
    """
    name = models.CharField(verbose_name='校区', max_length=64)
    address = models.CharField(verbose_name='详细地址', max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name


class ClassList(models.Model):
    """
    班级表
    """
    course = models.CharField("课程名称", max_length=64, choices=course_choices)
    semester = models.IntegerField("学期")
    campuses = models.ForeignKey('Campus', verbose_name="校区")
    price = models.IntegerField("学费", default=10000)
    memo = models.CharField('说明', blank=True, null=True, max_length=100)
    start_date = models.DateField("开班日期")
    graduate_date = models.DateField("结业日期", blank=True, null=True)
    teachers = models.ManyToManyField('UserProfile', verbose_name="老师")
    class_type = models.CharField(choices=class_type_choices, max_length=64, verbose_name='班额及类型', blank=True,
                                  null=True)

    class Meta:
        unique_together = ("course", "semester", 'campuses')

    def __str__(self):
        return '{}-{}'.format(self.get_course_display(), self.semester)


class ConsultRecord(models.Model):
    """
    跟进记录表
    """
    customer = models.ForeignKey('Customer', verbose_name="所咨询客户")
    note = models.TextField(verbose_name="跟进内容...")
    status = models.CharField("跟进状态", max_length=8, choices=seek_status_choices, help_text="选择客户此时的状态")
    consultant = models.ForeignKey("UserProfile", verbose_name="跟进人", related_name='records')
    date = models.DateTimeField("跟进日期", auto_now_add=True)
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)


class Enrollment(models.Model):
    """
    报名表
    """

    why_us = models.TextField("为什么报名", max_length=1024, default=None, blank=True, null=True)
    your_expectation = models.TextField("学完想达到的具体期望", max_length=1024, blank=True, null=True)
    contract_agreed = models.BooleanField("我已认真阅读完培训协议并同意全部协议内容", default=False)
    contract_approved = models.BooleanField("审批通过", help_text="在审阅完学员的资料无误后勾选此项,合同即生效", default=False)
    enrolled_date = models.DateTimeField(auto_now_add=True, verbose_name="报名日期")
    memo = models.TextField('备注', blank=True, null=True)
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)
    customer = models.ForeignKey('Customer', verbose_name='客户名称')
    school = models.ForeignKey('Campus')
    enrolment_class = models.ForeignKey("ClassList", verbose_name="所报班级")

    class Meta:
        unique_together = ('enrolment_class', 'customer')


class PaymentRecord(models.Model):
    """
    缴费记录表
    """
    pay_type = models.CharField("费用类型", choices=pay_type_choices, max_length=64, default="deposit")
    paid_fee = models.IntegerField("费用数额", default=0)
    note = models.TextField("备注", blank=True, null=True)
    date = models.DateTimeField("交款日期", auto_now_add=True)
    course = models.CharField("课程名", choices=course_choices, max_length=64, blank=True, null=True, default='N/A')
    class_type = models.CharField("班级类型", choices=class_type_choices, max_length=64, blank=True, null=True,
                                  default='N/A')
    enrolment_class = models.ForeignKey('ClassList', verbose_name='所报班级', blank=True, null=True)
    customer = models.ForeignKey('Customer', verbose_name="客户")
    consultant = models.ForeignKey('UserProfile', verbose_name="销售")
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)

    status_choices = (
        (1, '未审核'),
        (2, '已审核'),
    )
    status = models.IntegerField(verbose_name='审核', default=1, choices=status_choices)

    confirm_date = models.DateTimeField(verbose_name="确认日期", null=True, blank=True)
    confirm_user = models.ForeignKey(verbose_name="确认人", to='UserProfile', related_name='confirms', null=True,
                                     blank=True)


class CourseRecord(models.Model):
    """课程记录表"""
    day_num = models.IntegerField("节次", help_text="此处填写第几节课或第几天课程...,必须为数字")
    date = models.DateField(auto_now_add=True, verbose_name="上课日期")
    course_title = models.CharField('本节课程标题', max_length=64, blank=True, null=True)
    course_memo = models.TextField('本节课程内容', max_length=300, blank=True, null=True)
    has_homework = models.BooleanField(default=True, verbose_name="本节有作业")
    homework_title = models.CharField('本节作业标题', max_length=64, blank=True, null=True)
    homework_memo = models.TextField('作业描述', max_length=500, blank=True, null=True)
    scoring_point = models.TextField('得分点', max_length=300, blank=True, null=True)
    re_class = models.ForeignKey('ClassList', verbose_name="班级")
    teacher = models.ForeignKey('UserProfile', verbose_name="讲师", related_name='t_course_record')
    recorder = models.ForeignKey('UserProfile', verbose_name="记录者", related_name='r_course_record')

    class Meta:
        unique_together = ('re_class', 'day_num')


class StudyRecord(models.Model):
    """
    学习记录
    """

    attendance = models.CharField("考勤", choices=attendance_choices, default="checked", max_length=64)
    score = models.IntegerField("本节成绩", choices=score_choices, default=-1)
    homework_note = models.CharField(max_length=255, verbose_name='作业批语', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField("备注", max_length=255, blank=True, null=True)
    course_record = models.ForeignKey('CourseRecord', verbose_name="某节课程")
    student = models.ForeignKey('Customer', verbose_name="学员")

    class Meta:
        unique_together = ('course_record', 'student')

```

# 2. 展示页面

## 2.1 `__str__`方法

1. str方法**必须有返回值**，否则会报错

```python
# 用户信息的 model
class Customer(models.ModelForm):   
  	def __str__(self):
        if self.name:
            return self.name
        return 'None'
```

## 2.2 `__init__`方法

1. 在forms类中使用**初始化方法**
2. 一般重写初始化方法时，需要使用父类的**init**方法

```python
# forms.py
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            if not isinstance(i, (MultiSelectFormField, DateField)):
                i.widget.attrs['class'] = 'form-control'
                print(i, type(i))
            if isinstance(i, DateField):
                i.widget = forms.TextInput(attrs={'placeholder': "YYYY-MM-DD", 'autocomplete': "off", 'type': 'date'})

```

## 2.3 模版文件

1. 此时的字段对象是BoundField对象，其中self.field = field。
2. for 循环中的对象不是原来的**field**
3. 有for循环的一般都有`__iter__`方法
4. self['name'] 会触发`__getitem__`方法
5. 通过判断字段的错误字典，定义显示样式

```django
{# ModelForm通过for循环生成各个字段 #}
{% for i in obj %}
		<div class="form-group col-sm-3"  style="text-align: right">
				<label for="{{ i.id_for_label }}" {% if not i.field.required %}style="color:#8f8f8f"{% endif %}>{{ i.label }}:</label>
		</div>
		<div class="form-group col-sm-7 {% if i.errors %}has-error{% endif %}"{% if not i.field.required %} style="color:#8f8f8f"{% endif %}>
      {{ i }}
			<span class="help-block">{{ i.errors.0 }}</span>
		</div>
{% endfor %}
```

## 2.3 自定义方法

1. 后端处理好html标签样式之后作为字符串传递到前端，需要使用**mark_safe()**标记
2. 如果ModelForm中使用choices=((1, '男'),(2, '女'))，后端处理需要使用`对象.get_字段名_display()`方法，前端使用`对象.get_字段名_display`

```python
    def show_status(self):
        info = {'signed': 'green', 'unregistered': 'red', 'studying': 'skyblue', 'paid_in_full': 'gold'}
        return mark_safe('<span style="color:white; background-color: {};padding:5px">{}</span>'.format(info.get(self.status), self.get_status_display()))
```

## 2.4 中间件处理请求

1. 需要对**admin**账户，**以及登陆**放行
2. 如果后续需要使用一些数据，可以在通过验证之后，把数据封装到**request**对像中，即**reques.变量名 = 值**

```python
# crm.middlewares下的middleware.py
# 登陆校验
class CheckLogin(MiddlewareMixin):
    def process_request(self, request):
        url = request.path_info
        if url in [reverse('login'), reverse('reg')]:
            return
        if url.startswith('/admin'):
            return
        user = request.session.get('is_login')
        if not user:
            return redirect(reverse('login') + '?return_url={}'.format(url))
        obj = models.UserProfile.objects.filter(pk=request.session.get('user_id')).first()
        if obj:
            request.user_obj = obj
```

## 2.5 共用一个html文件

- 路由设计

```python
# urls.py
# 网址不同，经由一个view函数处理
url(r'^add_customer/', views.modify_customer, name='add_customer'),
url(r'^edit_customer/(\d+)', views.modify_customer, name='edit_customer'),
```

- 共用views函数

```python
# views.py
def modify_customer(request, pk=None):
    user_obj = models.Customer.objects.filter(pk=pk).first()
    obj = CustomerForm(instance=user_obj)
    if request.method == 'POST':
        obj = CustomerForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            return redirect('show_customer')
    title = '修改客户' if pk else '新增客户'
    return render(request, 'modify_customer.html', {'obj': obj, 'title': title})
```

1. form_obj = CustomerForm(**data**=request.POST, **instance**=user_obj)
   - data表示实例化需要的数据，instance表示html页面渲染用的数据，默认为None

# 3. 公私户转换









# 附录：

## 1. Django中模块的导入

### 1.1 form组件相关(3)

```python
# form 组件的导入
from django import forms
# form校验的异常导入
from django.core.exceptions import ValidationError
# MultiSelectFormField, 第三方模块，pip3 install django-multiselectfield
from multiselectfield.forms.fields import MultiSelectFormField
```

### 1.2 URL相关(1)

```python
# url配置，路由分发
from django.conf.urls import url, include
```

### 1.3 Model相关(4)

```python
# 对象关系映射模型
from django.db import models
# 聚合分组相关，以及 F，Q查询
from django.db.models import F, Q, Max, Min, Avg, Count, Sum
# 事务
from django.db import transcation
# 自定义方法中的 html 标签，在进行不转义显示
from django.utils.safestring import mark_safe
```

### 1.4 Template相关(2)

```python
# 导入模版
from django import template
register = template.Library()
# html标签取消转义
from django.utils.safestring import mark_safe
```

### 1.5 View相关(5)

```python
# 导入视图
from django.views import View
# 响应以及路由的反解析
from django.shortcuts import render, redirect, HttpResponse, reverse
# HttpResponse的导入
from django.http import HttpResponse
# JsonResponse的导入, 通常用于dict类型，如果是list，需要指定safe=False， 默认为True
from django.http.response import JsonResponse
		return HttpResponse(data，content-type = 'applicatoin/json')

# 模版的响应
from django.template.response import TemplateResponse
```

### 1.6 装饰器相关(2)

```python
# 给CBV加装饰器
from django.utils.decorators import method_decorator
# csrf中的装饰器
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
```

### 1.7 中间件相关(1)

```python
from django.utils.deprecation import MiddleMixin
```

### 1.8 admin相关(2)

```python
from django.contrib import admin
from app import models
admin.site.register(models.UserProfile)
```

### 1.9 app相关(1)

```python
from django.app import AppConfig
class App01Config(AppConfig):
		name='app01'
```









