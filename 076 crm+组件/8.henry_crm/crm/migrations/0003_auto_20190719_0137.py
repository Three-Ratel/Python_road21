# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-18 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190717_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='contract_agreed',
            field=models.BooleanField(default=False, verbose_name='已阅读完培训协议并同意'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Campus', verbose_name='学校'),
        ),
    ]
