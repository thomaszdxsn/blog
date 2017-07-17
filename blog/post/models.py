from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

from uuslug import uuslug

from core.models import TimeStampAbsClass, PostPublishedManager


class Post(TimeStampAbsClass):
    """博客文章"""
    author = models.ForeignKey(User, verbose_name="作者",
                               on_delete=models.CASCADE)
    title = models.CharField("标题", max_length=60, db_index=True)
    slug = models.CharField(max_length=100)
    content = models.TextField("内容")
    publish_time = models.DateTimeField("发表时间", default=timezone.now)
    image = models.ImageField(upload_to="post/%Y/%m/%d",
                              default="/image/136/120/")

    objects = models.Manager()
    published = PostPublishedManager()

    class Meta:
        ordering = ("-created",)
        verbose_name = verbose_name_plural = "博客文章"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self,
                           max_length=100, start_no=2)
        super().save(*args, **kwargs)



