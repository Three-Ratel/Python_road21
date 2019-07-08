#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http.request import QueryDict
from django.template import Library
from django.urls import reverse

register = Library()


@register.simple_tag
def reverse_url(request, name, *args, **kwargs):
    next = request.get_full_path()
    print(next)
    url = reverse(name, args=args, kwargs=kwargs)
    qd = QueryDict(mutable=True)
    qd['next'] = next
    return '{}?{}'.format(url, qd.urlencode())
