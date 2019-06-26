#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MtM.settings')
django.setup()
from app01 import models
from django.db.models import Count, Sum, Avg, Max, Min

# obj = models.Book.objects.all().aggregate(Max('price'), Avg('price'), Count('price'), Min('price'), Sum('price'))
# print(obj)

# obj = models.Book.objects.aggregate(Max('price'))
# print(obj)


# 分组
# obj = models.Publisher.objects.values('name').annotate(Max('xxx__price'))
# for i in obj:
#     print(i)

# # 统计每本书的作者个数
# obj = models.Book.objects.values('title').annotate(Count('xxx__name'))
# for i in obj:
#     print(i)

# # 统计出每个出版社买的最便宜的书的价格
# obj = models.Publisher.objects.values('name').annotate(Min('xxx__price'))
# for i in obj:
#     print(i)
# 统计不止一个作者的图书
# obj = models.Book.objects.values('title').annotate(count=Count('author__id')).filter(count__gt=1)
# print(obj)
# ret = models.Book.objects.annotate(count=Count('author__id')).filter(count__gt=1)
# print(ret)

# 根据一本图书作者数量的多少对查询集 QuerySet进行排序
# obj = models.Author.objects.annotate(count=Count('books__id')).order_by('count')
# print(obj)

# obj = models.Author.objects.annotate(Sum('books__price'))
# print(obj)


