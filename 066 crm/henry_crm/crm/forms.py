#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
            'mobile': forms.TextInput(attrs={'placeholder': "您的手机号", 'autocomplete': "off", }),
        }
        error_messages = {
            'username': {
                'required': '信息不能为空',
                'invalid': '邮箱格式不正确',
            }
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        # print(self.cleaned_data.get('department'))
        if password == re_password:
            md = hashlib.md5(b'sajdfkh')
            md.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md.hexdigest()
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
