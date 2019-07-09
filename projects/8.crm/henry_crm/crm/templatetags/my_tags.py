#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http.request import QueryDict
from django.template import Library
from django.urls import reverse

register = Library()


@register.simple_tag
def reverse_url(request, name, *args, **kwargs):
    next = request.get_full_path()
    url = reverse(name, args=args, kwargs=kwargs)
    qd = QueryDict(mutable=True)
    qd['next'] = next
    # print(next)
    # print(qd, qd.urlencode())
    return '{}?{}'.format(url, qd.urlencode())
