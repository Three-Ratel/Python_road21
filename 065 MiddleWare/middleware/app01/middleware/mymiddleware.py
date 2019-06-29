#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):

    def process_request(self, request):
        print('This is Md1 process_request')
        # print(id(request))
        # return HttpResponse("here's process_request method of Md1")

    def process_view(self, *args, **kwargs):
        print('This is Md1 process_view')

    def process_response(self, request, response):
        print('This is Md1 process_response')
        return response

    def process_exception(self, request, exception):
        print('This is Md1 process_response')
        print(exception)
        return HttpResponse('错误')

    def process_template_response(self, request, response):
        print("here's process_template_response of Md1")
        response.context_data['name'] = 'henry'
        return response


class Md2(MiddlewareMixin):

    def process_request(self, request):
        print('This is Md2 process_request, Md2')
        # print(id(request))
        # return HttpResponse("here's process_request method of Md2")

    def process_view(self, *args, **kwargs):
        print('This is Md2 process_view, Md2')

    def process_response(self, request, response):
        print('This is Md2 process_response, Md2')
        return response

    def process_exception(self, request, exception):
        print('This is Md2 process_response, Md2')
        print(exception)
        return HttpResponse('错误,Md2')

    def process_template_response(self, request, response):
        print("here's process_template_response of Md2")
        response.template_name='test.html'
        return response
