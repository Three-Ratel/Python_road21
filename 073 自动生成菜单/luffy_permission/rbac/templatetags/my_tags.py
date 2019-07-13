from django.template import Library
import re
from django.conf import settings
register = Library()


@register.inclusion_tag('menu.html')
def generator(request):
    menus = request.session.get(settings.MENU_SESSION_KEY)
    url = request.path
    for i in menus:
        if re.match(r'{}$'.format(i['url']), url):
            i['class'] = 'active'
            break
    return {'menus': menus, 'request': request}
