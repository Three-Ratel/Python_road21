import re

from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag('menu.html')
def generator(request):
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
    return {'menu_list': menu_dic.values()}