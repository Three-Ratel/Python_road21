# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "henry_crm.settings")
django.setup()
from crm.models import Customer

for i in range(1, 1000):
    Customer.objects.create(qq='9124123{}'.format(i),
                            name='oleg{}'.format(i),
                            sex='male' if i % 3 else 'female',
                            source= 'baidu_ads' if i % 3 else 'website',
                            course= 'PythonFullStack' if i % 2 else 'Linux',
                            class_type='fulltime' if i % 2 else 'weekend',
                            status='studying' if i % 2 else 'signed',
                            next_date='2019-08-07',
                            consultant_id= 5 if i%3 else 6,
                            )


