from django.shortcuts import render, redirect, HttpResponse

from app1 import models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if models.User.objects.filter(username=username, pwd=pwd):
            return redirect('/list_student/')
    return render(request, 'login.html')


def logout(request):
    return redirect('/login/')

# 学生管理函数
def list_student(request):
    all_student = models.Student.objects.all()
    return render(request, 'list_student.html', {'all_student': all_student})


def add_student(request):
    error = ''
    if request.method == 'POST':
        name = request.POST.get('stu_name')
        age = request.POST.get('stu_age')
        gender = request.POST.get('stu_gender')
        grade_id = request.POST.get('id')
        if not (name and age and gender):
            error = '学生信息不完整'
        if models.Student.objects.filter(name=name):
            error = '学生信息已存在'
        if not error:
            models.Student.objects.create(name=name, age=age, gender=gender, grade_id=grade_id)
            return redirect('/list_student/')
    all_grade = models.Grade.objects.all()
    return render(request, 'add_student.html', {'error': error, 'all_grade': all_grade})


def del_student(request):
    sid = request.GET.get('id')
    obj = models.Student.objects.filter(sid=int(sid))
    obj.delete()
    return redirect('/list_student/')


def edit_student(request):
    error = ''
    sid = request.GET.get('id')
    student = models.Student.objects.get(sid=sid)
    all_grade = models.Grade.objects.all()
    if request.method == 'POST':
        name = request.POST.get('stu_name')
        age = request.POST.get('stu_age')
        gender = request.POST.get('stu_gender')
        grade_id = request.POST.get('id')
        if not (name and age and gender):
            error = '学生信息不完整'
        elif models.Student.objects.filter(name=name, age=age, gender=gender, grade_id=grade_id):
            error = '未做任何修改'
        if not error:
            student.name = name
            student.age = age
            student.gender = gender
            student.grade_id = grade_id
            student.save()
            return redirect('/list_student/')
    return render(request, 'edit_student.html', {'student': student, 'all_grade': all_grade, 'error': error})


# 班级管理函数
def list_grade(request):
    all_grade = models.Grade.objects.all().order_by('title')
    return render(request, 'list_grade.html', {'all_grade': all_grade})


def add_grade(request):
    error = ''
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        if not class_name:
            error = '请输入班级名称'
        if models.Grade.objects.filter(title=class_name):
            error = '班级名称不能重复'
        if not error:
            models.Grade.objects.create(title=class_name)
            return redirect('/list_grade/')
    return render(request, 'add_grade.html', {'error': error})


def del_grade(request):
    gid = request.GET.get('id')
    obj = models.Grade.objects.filter(id=gid)
    if obj: obj.delete()
    return redirect('/list_grade/')


def edit_grade(request):
    error = ''
    gid = request.GET.get('id')
    grade = models.Grade.objects.get(id=gid)
    if request.method == 'POST':
        title = request.POST.get('class_name')
        if not title:
            error = '请输入班级名称'
        if models.Grade.objects.filter(title=title):
            error = '班级名称已存在，请重新输入'
        if not error:
            grade.title = title
            grade.save()
            return redirect('/list_grade/')
    return render(request, 'edit_grade.html', {'grade': grade, 'error': error})
