#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MtM.settings')
django.setup()
from app01 import models
from django.db import transaction
try:
    with transaction.atomic():
        models.Book.objects.create(title='xx', price=20, pub_id=2, sale=10, inventory=90)
        # int('s')
        models.Book.objects.filter(title='xx').update(title='xxxxxxxxxxxx')
except Exception as e:
    print(e)





