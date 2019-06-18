#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='henry')
def add_(value, arg):
    return '{}-{}'.format(value, arg)
