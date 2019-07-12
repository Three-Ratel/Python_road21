from django.shortcuts import render, redirect

from rbac import models


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        if obj:
            request.session['is_login'] = True
            permissions = obj.roles.exclude(permissions__url__isnull=True)
            permissions_url = permissions.values('permissions__url').distinct()
            menu_list = obj.roles.filter(permissions__url__isnull=False, permissions__is_menu=True).values(
                'permissions__is_menu', 'permissions__title', 'permissions__url', 'permissions__icon')
            request.session['permissions'] = list(permissions_url)
            request.session['menu_list'] = list(menu_list)
            # print(menu_list)
            return redirect('index')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
