#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin

from crm import models


class CheckLogin(MiddlewareMixin):

    def process_request(self, request):
        url = request.path_info
        # if url in [reverse('login'), reverse('reg')]:
        #     return
        # if url.startswith('/admin'):
        #     return

        user = request.session.get('is_login')
        if not user:
            return redirect(reverse('login') + '?return_url={}'.format(url))
        obj = models.UserProfile.objects.filter(pk=request.session.get('user_id')).first()
        if obj:
            request.user_obj = obj
