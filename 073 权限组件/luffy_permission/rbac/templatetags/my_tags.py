from django.template import Library

register = Library()


@register.inclusion_tag('menu.html')
def generator(request):
    menu_list = request.session.get('menu_list')
    return {'menu_list': menu_list, 'request': request}
