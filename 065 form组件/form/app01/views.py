from django import forms
# from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponse, render


from app01 import models

def check(value):
    if not value:
        raise ValidationError('用户名不合法')


# 手写实现form表单验证
# def register(request):
#     msg = ''
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         print(username, len(username))
#         if len(username) < 6:
#             msg = '用户名长度至少6位'
#         else:
#             # 把用户名和密码写入数据库
#             return HttpResponse('注册成功')
#
#     return render(request, 'register.html', {'msg': msg})
# from django import forms
# 示例1
# class RegForm(forms.Form):
#     username = forms.CharField()
#     pwd = forms.CharField()
#
#
# def register(request):
#     obj = RegForm()
#     if request.method == 'POST':
#         obj = RegForm(request.POST)
#         if obj.is_valid():
#             return HttpResponse('注册成功')
#     return render(request, 'register.html', {'obj': obj})
# 字段示例
class RegForm(forms.Form):
    # username = forms.CharField(
    #     min_length=5,
    #     label='用户名',
    #     initial='henry',
    #     error_messages={
    #         'required': '不能为空',
    #         'invalid': '格式有误',
    #         'min_length': '用户名最短6位'
    #     }
    # )
    # pwd = forms.CharField(
    #     min_length=6,
    #     label='密码',
    #     initial='123456',
    #     widget=forms.PasswordInput,
    # )
    # gender = forms.ChoiceField(
    #     choices=((0, 'female'), (1, 'male'), (3, 'secret')),
    #     label='性别',
    #     initial=3,
    #     widget=forms.widgets.RadioSelect()
    # )
    # hobby = forms.ChoiceField(
    #     choices=((1, 'travelling'), (2, 'reading'), (3, 'listening'),),
    #     label='爱好',
    #     initial=3,
    #     widget=forms.widgets.Select(),
    # )
    # hobby = forms.MultipleChoiceField(
    #     choices=(('1', 'travelling'), ('2', 'reading'), ('3', 'listening'),),
    #     label='爱好',
    #     initial=['3'],
    #     widget=forms.widgets.SelectMultiple(),
    # )
    #
    # keep = forms.fields.ChoiceField(
    #     label='是否记住密码',
    #     initial='checked',
    #     widget=forms.widgets.CheckboxInput(),
    # )

    #     多选checkbox

    # hobby = forms.fields.MultipleChoiceField(
    #     choices=((1, 'travelling'), (2, 'reading'), (3, 'listening'),),
    #     label="爱好",
    #     initial=[1, 3],
    #     widget=forms.widgets.CheckboxSelectMultiple
    # )
    # 动态多选
    hobby = forms.ModelChoiceField(
        queryset=models.Hobby.objects.all()
    )

    # 动态多选二
    # hobby = forms.MultipleChoiceField(
    #     choices=models.Hobby.objects.all().values_list('pk', 'name')
    # )
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['hobby'].choices = models.Hobby.objects.values_list()

    # 校验手机号
    # phone = forms.CharField(
    #     validators=[RegexValidator(r'1[3-9]\d{9}$', '手机号不合法')]
    # )
    username = forms.CharField(label='用户名')

    pwd = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput,
    )
    re_pwd = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput,
    )

    def clean_username(self):
        if 'o' in self.cleaned_data.get('username'):
            raise ValidationError('用户名不合法。。。。。')

    def clean(self):
        if not self.cleaned_data.get('pwd') == self.cleaned_data.get('re_pwd'):
            self.add_error('re_pwd','两次密码不一致')
            raise ValidationError('两次密码不一致')


def register(request):
    obj = RegForm()
    if request.method == 'POST':
        obj = RegForm(data=request.POST)
        if obj.is_valid():
            return HttpResponse('注册成功')
    return render(request, 'register.html', {'obj': obj})
