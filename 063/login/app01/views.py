from django.shortcuts import render, redirect
# from django.utils.decorators import method_decorator
from django.views import View


# def login_status(func):
#     def inner(request, table, *args, **kwargs):
#         if not request.COOKIES.get('login', None):
#             return redirect('/login/?return_url=/{}/'.format(table))
#         return func(request, table, *args, **kwargs)
#
#     return inner
#
#
# def login_status_fun(func):
#     def inner(request, *args, **kwargs):
#         # # 没有加盐
#         status = request.COOKIES.get('login')
#         # print(request.COOKIES)
#         # 加盐
#         # status = request.get_signed_cookie('login', default='', salt='xxx')
#         # print(request.get_signed_cookie)
#         if status != '1':
#             return redirect('/login/?return_url={}'.format(request.path_info))
#         return func(request, *args, **kwargs)
#
#     return inner
#
#
# class Login(View):
#
#     def get(self, request):
#         return render(request, 'login.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         pwd = request.POST.get('pwd')
#         if username == 'henry' and pwd == '123':
#             url = request.GET.get('return_url', 'index')
#             response = redirect('{}'.format(url))
#             # 不加盐
#             response.set_cookie('login', 1)
#             # # 给cookie加盐
#             # response.set_signed_cookie('login', 1, salt='xxx')
#             return response
#         return render(request, 'login.html', {'error': '用户名或密码错误'})
#
#
# def logout(request):
#     ret = render(request, 'login.html')
#     ret.set_cookie('login', '')
#     return ret
#
#
# @login_status_fun
# def index(request):
#     return render(request, 'index.html')
#
#
# @method_decorator(login_status, 'dispatch')
# class List_item(View):
#
#     def get(self, request, table):
#         return render(request, 'list_{}.html'.format(table))

# @method_decorator(login_status, 'dispatch')
# class Del_item(View):
#     def get(self, table):


# 装饰器函数
def login_status(func):
    def inner(request, *args, **kwargs):
        status = request.session.get('login')
        if status != 1:
            return redirect('/login/?return_url={}'.format(request.path_info))
        return func(request, *args, **kwargs)

    return inner


# 登陆处理
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'henry' and pwd == '123':
            # 设置session
            request.session['login'] = 1
            # request.session.set_expiry(10)


            request.session.clear_expired()



            url = request.GET.get('return_url', 'index')
            response = redirect('{}'.format(url))
            return response

        return render(request, 'login.html', {'error': '用户名或密码错误'})


# 登出处理
def logout(request):
    ret = render(request, 'login.html')
    request.session.delete()
    return ret


@login_status
def index(request):
    return render(request, 'index.html')


from django.conf import global_settings
