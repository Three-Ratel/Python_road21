from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse
from django.core.validators import RegexValidator
from app01 import models


# from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
# from django.utils.decorators import method_decorator
# decorations = [ensure_csrf_cookie, csrf_protect, ]
# @method_decorator(decorations, 'dispatch')
def checkname(value):
    if 'o' in value:
        raise ValidationError('用户名不能包含o')


class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名:',
        initial='henry',
        required=True,
        min_length=5,
        max_length=8,
        validators=[checkname],
        error_messages={
            'required': '用户名不能为空',
            'min_length': '用户名长度至5-8',
        }
    )
    pwd = forms.CharField(
        label='密码:',
        initial='123456',
        required=True,
        min_length=6,
        max_length=8,
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码长度长度在6-8之间',
        },
        widget=forms.widgets.PasswordInput,
    )
    re_pwd = forms.CharField(
        label='确认密码:',
        required=True,
        min_length=6,
        max_length=8,
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码长度长度在6-8之间',
        },
        widget=forms.widgets.PasswordInput,
    )
    phone = forms.CharField(
        label='联系方式:',
        required=True,
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号不合法'),],
    )

    def clean(self):
        if not self.cleaned_data.get('pwd') == self.cleaned_data.get('re_pwd'):
            self.add_error('re_pwd', '两次密码不一致')
        return self.cleaned_data

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if 'h' in username:
    #         raise ValidationError('用户名不合法')
    #     return username


def register(request):
    obj = RegForm()
    if request.method == 'POST':
        obj = RegForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data.get('username')
            pwd = obj.cleaned_data.get('pwd')
            phone = obj.cleaned_data.get('phone')
            print(username, pwd, phone)
            models.User.objects.create(username=username, pwd=pwd, phone=phone)
            return HttpResponse('注册成功')
    return render(request, 'register.html', {'obj': obj})
