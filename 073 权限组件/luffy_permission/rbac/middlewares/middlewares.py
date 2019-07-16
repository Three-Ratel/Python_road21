import re

from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.utils.deprecation import MiddlewareMixin


# 1. 注册rbacapp
# 2. 注册当前中间件
# 3. 在配置文件中，设置：豁免的url，EXEMPT_URL = []， 和 白名单列表：WHITE_LIST = []

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        path = request.path
        # print('白名单列表')
        for url in settings.WHITE_LIST:
            if re.match(url, path):
                return
        # print('校验登录状态')
        if not request.session.get('is_login'):
            return render(request, 'login.html')
        # print('豁免列表')
        
        for url in settings.EXEMPT_URL:
            if re.match(url, path): return

        permissions = request.session.get('permissions')
        # print('权限列表')
        for i in permissions:
            # print(i)
            if re.match(i.get('permissions__url'), path):
                return
        return HttpResponse('没有访问权限，请联系管理员')
