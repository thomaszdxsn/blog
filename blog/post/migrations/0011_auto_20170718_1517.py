# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 07:17
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20170718_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(verbose_name='内容'),
        ),
    ]