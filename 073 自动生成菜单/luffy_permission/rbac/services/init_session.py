from django.conf import settings


def init_session(request, obj):
    request.session['is_login'] = True
    permissions = obj.roles.exclude(permissions__url__isnull=True).values('permissions__url',
                                                                          'permissions__title',
                                                                          'permissions__menu__icon',
                                                                          'permissions__menu__title',
                                                                          'permissions__menu_id').distinct()

    permission_list = []
    menu_dic = {}

    # 构造权限列表，和菜单字典
    for i in permissions:
        permission_list.append(i.get('permissions__url'))
        menu_id = i.get('permissions__menu_id')
        if menu_id:
            if not menu_dic.get(menu_id):
                menu_dic[menu_id] = {
                    'title': i.get('permissions__menu__title'),
                    'icon': i.get('permissions__menu__icon'),
                    'children': [{'title': i.get('permissions__title'),
                                  'url': i.get('permissions__url')}]
                }
            else:
                menu_dic[menu_id]['children'].append(
                    {'title': i.get('permissions__title'),
                     'url': i.get('permissions__url')})
        # 权限列表
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # 菜单列表
    request.session[settings.MENU_SESSION_KEY] = menu_dic