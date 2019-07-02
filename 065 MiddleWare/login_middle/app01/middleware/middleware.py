#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class CheckStatus(MiddlewareMixin):
    def process_request(self, request):
        if request.session.get('login') != '1':
            url = request.path_info
            # print(url)
            if url != '/login/':
                return redirect('/login/?return_url={}'.format(url))
