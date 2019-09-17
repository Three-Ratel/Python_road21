from django.core.signals import request_started
from django.shortcuts import HttpResponse


# Create your views here.

# 方式一
def callback(sender, **kwargs):
    print("哈哈哈，请求来了。。。")
    print(sender, kwargs)


request_started.connect(callback)


def index(request):
    print('here')
    return HttpResponse('Index')


import django.dispatch

pizza_done = django.dispatch.Signal(providing_args=['toppings', 'size'])
