#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def show_a(value, arg):
    return mark_safe('<a href={}>{}</a>'.format(value, arg))


@register.filter(is_safe=True)
def show_b(value, arg):
    return '<a href={}>{}</a>'.format(value, arg)
