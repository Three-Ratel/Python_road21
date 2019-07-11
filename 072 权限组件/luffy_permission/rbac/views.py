from django.shortcuts import render, redirect

from rbac import models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        if obj:
            request.session['is_login'] = True
            permissions = obj.roles.exclude(permissions__url__isnull=True).values('permissions__url').distinct()
            request.session['permissions'] = list(permissions)
            return redirect('index')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
