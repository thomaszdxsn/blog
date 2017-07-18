# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20170718_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ('index',), 'verbose_name_plural': '轮播图', 'verbose_name': '轮播图'},
        ),
    ]
