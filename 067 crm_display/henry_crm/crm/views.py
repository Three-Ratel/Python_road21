import hashlib

from django.db.models import F
from django.shortcuts import render, redirect, reverse

from crm import models
from crm.forms import RegForm


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
            return redirect('customer_list')
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

items = models.Customer.objects.all()


def customer_list(request):
    # all_item = models.Customer.objects.all()
    # obj = Pagenation(request, len(all_item))
    # return render(request, 'customer_list.html', {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    """使用django的分页器"""

    paginator = Paginator(items, 10)
    page = request.GET.get('page')
    try:
        all_item = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_item = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_item = paginator.page(paginator.num_pages)
    return render(request, 'customer_list.html', {'all_item': all_item})
    # return render(request, 'customer_list.html', {'all_item': p.page(page).object_list, 'all_page': })
