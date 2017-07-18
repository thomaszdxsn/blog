# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('index', models.IntegerField(verbose_name='顺序')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='输入逗号分割的标签串', to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='post',
            field=models.OneToOneField(to='post.Post', verbose_name='文章'),
        ),
    ]
