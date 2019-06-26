#!/usr/bin/env python
# -*- coding:utf-8 -*-
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MtM.settings')
django.setup()
from app01 import models
from django.db.models import Q

# obj = models.Book.objects.filter(sale__gt=F('inventory'))
# print(obj)


# obj = models.Book.objects.filter(pub_id=1).update(pub_id=2)
# print(obj)

obj = models.Book.objects.filter(Q(price__lt=110), Q(price__gt=80))
print(obj)
