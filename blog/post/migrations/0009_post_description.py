# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20170718_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='简评'),
        ),
    ]
