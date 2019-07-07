import hashlib

from django.db.models import F
from django.shortcuts import render, redirect, reverse, HttpResponse

from crm import models
from crm.forms import RegForm, CustomerForm
from utils.pagenation import Pagenation


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
            url = request.GET.get('return_url')
            if url: ret = redirect(url)
            ret = redirect('customer')
            request.session['user_id'] = obj.pk
            request.session['is_login'] = True
            return ret
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def logout(request):
    request.session['is_login'] = ''
    ret = redirect('login')
    return ret


def customer_list(request):
    url = request.path
    if url == reverse('customer'):
        all_item = models.Customer.objects.filter(consultant__isnull=True)
    else:
        all_item = models.Customer.objects.filter(consultant_id=request.user_obj.pk)
    obj = Pagenation(request, len(all_item))
    return render(request, 'list_customer.html', {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    # """使用django的分页器"""
    # from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    # items = models.Customer.objects.all()
    # paginator = Paginator(items, 10, orphans=3)
    # page = request.GET.get('page')
    # try:
    #     all_item = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     all_item = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     all_item = paginator.page(paginator.num_pages)
    # return render(request, 'list_customer.html', {'all_item': all_item})


def modify_customer(request, pk=None):
    user_obj = models.Customer.objects.filter(pk=pk).first()
    obj = CustomerForm(instance=user_obj)
    if request.method == 'POST':
        obj = CustomerForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            return redirect('show_customer')
    title = '修改客户' if pk else '新增客户'
    return render(request, 'modify_customer.html', {'obj': obj, 'title': title})


def del_item(request):
    pk = request.GET.get('pk')
    models.Customer.objects.filter(pk=pk).delete()
    return HttpResponse('ok')


