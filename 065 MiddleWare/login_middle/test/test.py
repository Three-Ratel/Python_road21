#!/usr/bin/env python
# -*- coding:utf-8 -*-
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login.settings")
django.setup()
from app01 import models

obj = models.Test.objects.filter(name__lt=23)
for i in obj:
    print(i.name, type(i.name))
