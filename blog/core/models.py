from django.db import models
from django.utils import timezone


class TimeStampAbsClass(models.Model):
    """时间戳抽象基类，包括对象创建时间和修改时间"""
    created = models.DateTimeField("创建时间", auto_now_add=True)
    modified = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        abstract = True


class PostPublishedManager(models.Manager):
    """获得发布时间早于现在的文章"""
    def get_queryset(self):
        return super().get_queryset().filter(publish_time__lte=timezone.now())

