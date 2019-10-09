# from django import forms
from django.shortcuts import render, redirect

from app01 import models


# class StuFrom(forms.Form):
#     s_name = forms.CharField(
#         label='学生姓名',
#         required=True,
#         error_messages={
#             'required': '不能为空',
#         }
#     )
#
#     score = forms.IntegerField(
#         min_value=0,
#         max_value=100,
#         initial=0,
#         required=True,
#         error_messages={
#             'required': '不能为空',
#         }
#     )


def list_student(request):
    all_item = models.Student.objects.all()
    return render(request, 'list_student.html', {'all_item': all_item})


def add_student(request):
    error = ''
    if request.method == 'POST':
        stu_name = request.POST.get('stu_name')
        stu_score = request.POST.get('stu_score')
        stu_class = request.POST.get('stu_class')
        if stu_class and stu_name and stu_score:
            if models.Student.objects.filter(s_name=stu_name):
                error = '学生信息已存在，请重新输入'
            else:
                if 0 <= int(stu_score) <= 100:
                    models.Student.objects.create(s_name=stu_name, score=stu_score, my_class_id=stu_class)
                    return redirect('/list_student/')
                else:
                    error = '成绩必须在0-100之间'
        else:
            error = '学生信息不完整'
    all_class = models.Classes.objects.all()
    return render(request, 'add_student.html', {'all_class': all_class, 'error': error})


def edit_student(request):
    error = ''
    pk = request.GET.get('pk')
    stu = models.Student.objects.get(pk=pk)
    all_class = models.Classes.objects.all()
    if request.method == "POST":
        stu_name = request.POST.get('stu_name')
        stu_socre = request.POST.get('stu_score')
        stu_class = request.POST.get('stu_class')
        obj = models.Student.objects.filter(pk=pk)
        if obj and stu_name and stu_socre and stu_class:
            if 0 <= int(stu_socre) <= 100:
                obj = obj[0]
                obj.s_name = stu_name
                obj.score = stu_socre
                obj.my_class_id = stu_class
                obj.save()
                return redirect('/list_student/')
            else:
                error = '成绩必须在0-100之间'
        else:
            error = '信息不能为空'
    return render(request, 'edit_student.html', {'stu': stu, 'all_class': all_class, 'error': error})


def del_student(request):
    pk = request.GET.get('pk')
    obj = models.Student.objects.filter(id=pk)
    if obj: obj.delete()
    return redirect('/list_student/')
