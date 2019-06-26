from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View


def login_status(func):
    def inner(request, *args, **kwargs):
        if not request.COOKIES.get('login', None):
            return redirect('/login/?return_url={}'.format(request.path_info))
        return func(request, *args, **kwargs)

    return inner


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'henry' and pwd == '123':
            url = request.GET.get('return_url')
            response = redirect('{}'.format(url))
            response.set_cookie('login', 1)
            return response
        return render(request, 'login.html', {'error': '用户名或密码错误'})


@login_status
def index(request):
    return render(request, 'index.html')


@method_decorator(login_status, 'dispatch')
class List_item(View):

    def get(self, request, table):
        print(table)
        return render(request, 'list_{}.html'.format(table))
