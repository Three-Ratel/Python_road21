from django.shortcuts import render, redirect, HttpResponse

from app01 import models


# 列出所有的出版社
def list_publisher(request):
    all_publisher = models.Publisher.objects.all()
    return render(request, 'list_publisher.html', {'all_publisher': all_publisher})


# 增加出版社
def add_publisher(request):
    error = ''
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        if models.Publisher.objects.filter(name=publisher_name):
            error = '出版社已存在'
        if not publisher_name:
            error = '内容不能为空'
        if not error:
            models.Publisher.objects.create(name=publisher_name)
            return redirect('/list_publisher/')
    return render(request, 'add_publisher.html', {'error': error})


# 删除出版社
def del_publisher(request):
    if request.method == 'GET':
        pk = request.GET.get('id')
        obj_li = models.Publisher.objects.filter(pk=pk)
        if obj_li: obj_li.delete()
        return redirect('/list_publisher/')


# 修改出版社
def edit_publisher(request):
    pk = request.GET.get('id')
    obj_li = models.Publisher.objects.filter(pk=pk)
    if not obj_li:
        return HttpResponse('编辑的信息不存在')

    error = ''
    obj = obj_li[0]
    if request.method == 'POST':
        name = request.POST.get('publisher_name')
        if not name:
            error = '内容不能为空'
        if models.Publisher.objects.filter(name=name):
            error = '出版社名称已存在'
        if obj.name == name:
            error = '未做修改'
        if not error:
            obj.name = name
            obj.save()
            return redirect('/list_publisher/')
    print(error)
    return render(request, 'edit_publisher.html', {'name': obj.name, 'error': error})
