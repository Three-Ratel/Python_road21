#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http.response import  HttpResponse
from django.utils.deprecation import MiddlewareMixin
from app01 import views

class Md1(MiddlewareMixin):

    def process_request(self, request):
        print('here is process_request')