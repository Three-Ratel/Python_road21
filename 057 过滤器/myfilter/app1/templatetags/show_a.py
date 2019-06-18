#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter
def show_a(value, arg):
    return '{}{}'.format(value, arg)





