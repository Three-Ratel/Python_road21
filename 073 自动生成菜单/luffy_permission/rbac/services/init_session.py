from django.conf import settings


def init_session(request, obj):
    request.session['is_login'] = True
    permissions = obj.roles.exclude(permissions__url__isnull=True).values(
        'permissions__url',
        'permissions__title',
        'permissions__menu__icon',
        'permissions__menu__title',
        'permissions__menu_id',
        'permissions__menu__weight',
        'permissions__parent_id',
        'permissions__id',
    ).distinct()

    # 构造权限和菜单字典
    permission_dic = {}
    menu_dic = {}
    for i in permissions:
        permission_dic[i['permissions__id']] = {
            'url': i.get('permissions__url'),
            'title': i.get('permissions__title'),

            'id': i.get('permissions__id'),
            'pid': i.get('permissions__parent_id'),
            # id 和 pid 用于访问二级菜单中的子菜单时，保持二级菜单处于活跃状态
        }

        menu_id = i.get('permissions__menu_id')
        if menu_id:
            if not menu_dic.get(menu_id):
                menu_dic[menu_id] = {
                    'title': i.get('permissions__menu__title'),
                    'icon': i.get('permissions__menu__icon'),
                    'weight': i.get('permissions__menu__weight'),
                    'children': [
                        {'title': i.get('permissions__title'),
                         'url': i.get('permissions__url'),
                         'id': i.get('permissions__id'),
                         }]
                }
            else:
                menu_dic[menu_id]['children'].append(
                    {'title': i.get('permissions__title'),
                     'url': i.get('permissions__url'),
                     'id': i.get('permissions__id'),
                     })
    # print(permissions)
    # print(permission_dic)
    # print(menu_dic)
    # 权限列表
    request.session[settings.PERMISSION_SESSION_KEY] = permission_dic
    # 菜单列表
    request.session[settings.MENU_SESSION_KEY] = menu_dic
