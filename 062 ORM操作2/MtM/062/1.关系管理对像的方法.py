#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MtM.settings')
django.setup()
from app01 import models

# 基于对象的反向查询
# obj = models.Author.objects.get(pk=2).books.all()
# print(obj)

# book = models.Book.objects.get(pk=1)
# obj = book.pub.name
# print(obj)


# obj = models.Book.objects.get(pk=2).author_set.all()
# print(obj)
#
# # books为author的多对多外键
# obj = models.Author.objects.get(pk=1).books.all()
# print(obj)

# author = models.Author.objects.filter(books__title='python之旅')
# print(author)

# obj = models.Book.objects.filter(author__name='echo')
# print(obj)


# obj = models.Book.objects.filter(xxx__name='echo')
# print(obj)

"""关系管理对像的方法"""
author = models.Author.objects.get(pk=1)
# set方法
# author.books.set([1, 2])
# author.books.set(models.Book.objects.filter(pk__gt=2))
# # add方法
# author.books.add(3)
# author.books.add(models.Book.objects.get(pk=2))
# # remove方法
# author.books.remove(3)
# author.books.remove(models.Book.objects.get(pk=2))
# # clear()
# author.books.clear()


# obj = author.books.create(title='科学上网', price=10, pub_id=1)
# print(obj)
#
# obj = models.Book.objects.get(pk=1).author_set.create(name='dean')
# print(obj)








