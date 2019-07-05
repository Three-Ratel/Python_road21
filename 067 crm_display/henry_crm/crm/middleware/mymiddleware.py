#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from crm import models


class CheckLogin(MiddlewareMixin):

    def process_request(self, request):
        user = request.COOKIES.get('user')
        url = request.path_info
        if not models.UserProfile.objects.filter(username=user):
            # print(models.UserProfile.objects.filter(username=user))
            if url != '/crm/login/':
                return redirect('/crm/login/?return_url={}'.format(url))
