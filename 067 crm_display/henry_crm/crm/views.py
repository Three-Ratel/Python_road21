import hashlib

from django.db.models import F
from django.db.models import Q
from django.shortcuts import render, redirect, reverse

from crm import models
from crm.forms import RegForm, AddCustomer
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
            ret = redirect(url)
            ret.set_cookie('user', request.POST.get('username'))
            return ret

        return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

items = models.Customer.objects.all()


def customer_list(request):
    all_item = models.Customer.objects.all()
    obj = Pagenation(request, len(all_item))
    return render(request, 'list_customer.html', {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    # """使用django的分页器"""

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


def add_customer(request):
    obj = AddCustomer()
    if request.method == 'POST':
        obj = AddCustomer(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('customer')
    return render(request, 'add_customer.html', {'obj': obj})


def show_customer(request):
    user = request.COOKIES.get('user')
    items = models.Customer.objects.filter(Q(consultant__username=user) | Q(consultant_id=None))
    obj = Pagenation(request, len(items))
    return render(request, 'show_customer.html', {'all_item': items[obj.start:obj.end], 'all_page': obj.show})
