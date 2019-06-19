#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag('page.html')
def sqr_list(num):
    li = []
    for i in range(1, num + 1):
        li.append(i * i)
    return {'num': li}
