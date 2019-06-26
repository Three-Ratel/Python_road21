#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MtM.settings')
django.setup()
from app01 import models
from django.db.models import Max

"""外键的方法"""
# # all方法
# pub = models.Publisher.objects.get(pk=1)
# obj = pub.books.all()
# print(obj)

# # set 和 add 方法
# pub.books.set(models.Book.objects.filter(pk__lte=3))
# pub.books.add(models.Book.objects.get(pk=4))

# remove 方法
# models.Publisher.objects.get(pk=1).books.remove(models.Book.objects.get(pk=4))

# models.Publisher.objects.get(pk=1).books.clear()

# models.Publisher.objects.get(pk=1).books.create(title='xxx', price=10)


