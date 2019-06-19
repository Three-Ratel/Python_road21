#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def join_str(*args, **kwargs):
    return '{}----{}'.format('*'.join(args), '+'.join(kwargs.values()))


@register.inclusion_tag('page.html')
def page(num):
    return {'num': range(1, num + 1)}
