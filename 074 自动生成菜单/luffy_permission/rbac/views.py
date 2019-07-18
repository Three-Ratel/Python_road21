from django.shortcuts import render, redirect

from rbac import models
from rbac.services.init_session import init_session


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        # print(obj, type(obj))
        if obj:
            # 登陆成功, 初始化登陆状态、权限和菜单的seesion信息
            init_session(request, obj)
            return redirect('index')
    return render(request, 'rbac/login.html')


def index(request):
    return render(request, 'rbac/index.html')
