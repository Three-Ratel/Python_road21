import hashlib

from django.db.models import F
from django.shortcuts import render, redirect, reverse

from crm import models
from crm.forms import RegForm
from rbac.services.init_permission import init_permission

def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            obj = form_obj.save()
            models.Department.objects.filter(pk=obj.department.pk).update(count=F('count') + 1)
            return redirect(reverse('login'))
    return render(request, 'reg.html', {'form_obj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md = hashlib.md5(b'sajdfkh')
        md.update(password.encode('utf-8'))
        md.hexdigest()
        obj = models.UserProfile.objects.filter(username=username, password=md.hexdigest(), is_active=True).first()
        if obj:
            init_permission(request, obj)
            url = request.GET.get('return_url')
            if url: ret = redirect(url)
            ret = redirect('customer')
            request.session['user_id'] = obj.pk
            return ret
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def logout(request):
    request.session['is_login'] = ''
    ret = redirect('login')
    return ret
