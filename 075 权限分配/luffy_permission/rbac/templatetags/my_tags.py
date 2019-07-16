from collections import OrderedDict

from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    # 一级菜单
    # menus = request.session.get(settings.MENU_SESSION_KEY)
    # url = request.path
    # for i in menus:
    #     if re.match(r'{}$'.format(i['url']), url):
    #         i['class'] = 'active'
    #         break
    # return {'menus': menus}

    # 二级菜单
    menu_dic = request.session.get(settings.MENU_SESSION_KEY)
    # print(menu_dic.values())
    # 通过有序字典，为一级菜单指定顺序
    od = OrderedDict()
    keys = sorted(menu_dic, key=lambda x: menu_dic[x]['weight'], reverse=True)
    for i in keys:
        od[i] = menu_dic[i]

    # 二级菜单样式
    for i in menu_dic.values():
        i['class'] = 'hide'
        for m in i['children']:
            # print(m['id'])
            if request.current_menu_id == m['id']:
                m['class'] = 'active'
                i['class'] = ''
    return {'menu_dic': od}


@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):
    return {'breadcrumb_list': request.breadcrumb_list}


@register.filter
def has_permission(request, name):
    if name in request.session.get(settings.PERMISSION_SESSION_KEY):
        return True
