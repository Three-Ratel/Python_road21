#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import DateField, BooleanField
from multiselectfield.forms.fields import MultiSelectFormField

from crm import models


class BSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields.values():
            if not isinstance(i, (MultiSelectFormField, DateField, BooleanField)):
                i.widget.attrs['class'] = 'form-control'
            if isinstance(i, DateField):
                i.widget = forms.TextInput(attrs={'placeholder': "YYYY-MM-DD", 'autocomplete': "off", 'type': 'date'})


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


class CustomerForm(BSForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
        widgets = {
            #     'qq': forms.TextInput(attrs={'placeholder': "QQ号", 'autocomplete': "off", 'label': 'QQ号码', }),
            #     'qq_name': forms.TextInput(attrs={'placeholder': "QQ昵称", 'autocomplete': "off", }),
            #     'name': forms.TextInput(attrs={'placeholder': "客户姓名", 'autocomplete': "off", }),
            #     'phone': forms.TextInput(attrs={'placeholder': '手机号', 'autocomplete': "off", }),
            #     'source': forms.Select(attrs={'placeholder': '来源渠道', 'autocomplete': "off", }),
            #     'customer_note': forms.Textarea(attrs={'placeholder': '备注', 'autocomplete': "off", }),
            #     'class_list': forms.SelectMultiple(attrs={'placeholder': '已报班级', 'autocomplete': "off", }),
        }


class ConsultRecordForm(BSForm):
    class Meta:
        model = models.ConsultRecord
        fields = '__all__'

    # def __init__(self, request, customer_id, *args, **kwargs):
    #     super(ConsultRecord, self).__init__(*args, **kwargs)
    #     if customer_id and customer_id != '0':
    #         self.fields['customer'].choices = [(i, str(i)) for i in models.Customer.objects.filter(pk=customer_id)]
    #     else:
    #         self.fields['customer'].choices = [('', '-------------')] +
    #         [(i.pk, str(i)) for i in request.user_obj.customers.all()]
    #     self.fields['consultant'].choices = [(request.user_obj.pk, request.user_obj)]

    def __init__(self, *args, **kwargs):
        super(ConsultRecordForm, self).__init__(*args, **kwargs)
        # 如果id为 0， 则表示新增任意客户的跟进记录
        # 不为0，则表示新增当前客户的跟进记录
        if self.instance.customer_id != '0':
            self.fields['customer'].choices = [(self.instance.customer.pk, self.instance.customer.name)]
        else:
            self.fields['customer'].choices = [('', '-------------')] + \
                                              [(i.pk, str(i)) for i in self.instance.consultant.customers.all()]
        # 限制为当前销售
        self.fields['consultant'].choices = [(self.instance.consultant.pk, self.instance.consultant)]


class EnrollmentForm(BSForm):
    class Meta:
        model = models.Enrollment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        # 限制客户为当前客户
        self.fields['customer'].choices = [(self.instance.customer_id, self.instance.customer)]
        # 从客户信息表中，读取班级列表
        self.fields['enrolment_class'].choices = [(i.pk, str(i)) for i in self.instance.customer.class_list.all()]
        # print(self.fields['customer'].choices, type(self.fields['customer'].choices))


class ClasslistForm(BSForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClasslistForm, self).__init__(*args, **kwargs)
        self.fields['teachers'].choices = [(i.pk, i) for i in models.UserProfile.objects.filter(department__name='销售部')]


class CourseRecordForm(BSForm):
    class Meta:
        model = models.CourseRecord
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseRecordForm, self).__init__(*args, **kwargs)
        self.fields['re_class'].choices = [(self.instance.re_class_id, self.instance.re_class)]
        self.fields['recorder'].choices = [(self.instance.recorder.pk, self.instance.recorder)]
        self.fields['teacher'].choices = [(i.pk, str(i)) for i in self.instance.re_class.teachers.all()]


class StudyRecordForm(BSForm):
    class Meta:
        fields = '__all__'
