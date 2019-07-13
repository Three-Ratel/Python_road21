from django.conf import settings


def init_session(request, obj):
    request.session['is_login'] = True
    permissions = obj.roles.exclude(permissions__url__isnull=True).values('permissions__url',
                                                                          'permissions__title',
                                                                          'permissions__icon',
                                                                          'permissions__is_menu').distinct()
    permission_list = []
    menu_list = []
    for i in permissions:
        permission_list.append(i.get('permissions__url'))

        if i.get('permissions__is_menu'):
            menu_list.append(
                {'url': i.get('permissions__url'),
                 'title': i.get('permissions__title'),
                 'icon': i.get('icon')})
    # 权限列表
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # 菜单列表
    request.session[settings.MENU_SESSION_KEY] = menu_list
