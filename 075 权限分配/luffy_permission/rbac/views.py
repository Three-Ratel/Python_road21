from django.db.models import Q
from django.shortcuts import render, redirect

from rbac import models
from rbac.forms import MenuForm, PermissionForm
from rbac.services.init_session import init_session


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        if obj:
            # 登陆成功, 初始化登陆状态、权限和菜单的seesion信息
            init_session(request, obj)
            return redirect('index')
    return render(request, 'rbac/login.html')


def index(request):
    return render(request, 'rbac/index.html')


def menu_list(request):
    mid = request.GET.get('mid')
    all_menu = models.Menu.objects.all().order_by('-weight')
    if not mid:
        all_permission = models.Permission.objects.all().order_by('weight')
    else:
        all_permission = models.Permission.objects.filter(Q(menu_id=mid) | Q(parent__menu_id=mid)).order_by('weight')
    """
    构造权限字典
        { id : {
                    children： [ {}  {} ]
             } 
        }
    """
    permission_dic = {}
    for i in all_permission:
        if not i.menu_id: continue
        # print(i.menu_id, '二级菜单')
        permission_dic[i.menu_id] = {
            'pk': i.pk,
            'title': i.title,
            'url': i.url,
            'name': i.name,
            'menu_id': i.menu_id,
            'menu': i.menu.title,
            'children': [],
        }
    # print(permission_dic)
    for i in all_permission:
        if i.menu_id: continue
        # print(i.parent.menu_id, '非菜单')
        if i.parent and i.parent.menu_id:
            permission_dic[i.parent.menu_id]['children'].append({
                'pk': i.pk,
                'title': i.title,
                'url': i.url,
                'name': i.name,
            })
        # else:
        #     permission_dic['others'] = {
        #         'pk': i.pk,
        #         'title': i.title,
        #         'url': i.url,
        #         'name': i.name,
        #     }
    # print(permission_dic)
    return render(request, 'rbac/menu_list.html',
                  {'all_menu': all_menu,
                   'all_permission': permission_dic.values(),
                   'mid': mid,
                   }
                  )


def menu_change(request, pk=None):
    obj = models.Menu.objects.filter(pk=pk).first()
    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('menu_list')
    return render(request, 'form.html', {'form_obj': form_obj})


def menu_del(request, obj, pk):
    obj = getattr(models, obj.capitalize())
    obj.objects.filter(pk=pk).delete()
    return redirect('menu_list')


def permission_change(request, pk=None):
    obj = models.Permission.objects.filter(pk=pk).first()
    form_obj = PermissionForm(instance=obj)
    if request.method == 'POST':
        form_obj = PermissionForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('menu_list')
    return render(request, 'form.html', {'form_obj': form_obj})
