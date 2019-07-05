#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
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
        # self._validate_unique = True
        super().clean()
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md = hashlib.md5(b'sajdfkh')
            md.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md.hexdigest()
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')


class AddCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
        widgets = {
            'qq': forms.TextInput(attrs={'placeholder': "QQ号", 'autocomplete': "off", 'label': 'QQ号码', }),
            'qq_name': forms.TextInput(attrs={'placeholder': "QQ昵称", 'autocomplete': "off", }),
            'name': forms.TextInput(attrs={'placeholder': "客户姓名", 'autocomplete': "off", }),
            'phone': forms.TextInput(attrs={'placeholder': '手机号', 'autocomplete': "off", }),
            'source': forms.Select(attrs={'placeholder': '来源渠道', 'autocomplete': "off", }),
            'customer_note': forms.TextInput(attrs={'placeholder': '备注', 'autocomplete': "off", }),
            'consultant': forms.Select(attrs={'placeholder': '销售', 'autocomplete': "off", }),
            'class_list': forms.SelectMultiple(attrs={'placeholder': '已报班级', 'autocomplete': "off", }),
        }

    birthday = forms.DateField(
        label='出生日期',
        widget=forms.widgets.SelectDateWidget,
    )
    next_date = forms.DateField(
        label='预计下次跟进时间',
        initial=datetime.datetime.now(),
        widget=forms.widgets.SelectDateWidget,
    )
    course = forms.ChoiceField(
        label='咨询课程',
        widget=forms.widgets.CheckboxSelectMultiple,
    )
