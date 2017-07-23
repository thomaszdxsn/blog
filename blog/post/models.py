from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

from uuslug import uuslug
from taggit.managers import TaggableManager
from django_markdown.models import MarkdownField

from core.models import TimeStampAbsClass, PostPublishedManager


class Post(TimeStampAbsClass):
    """博客文章"""
    author = models.ForeignKey(User, verbose_name="作者",
                               on_delete=models.CASCADE)
    title = models.CharField("标题", max_length=60, db_index=True)
    slug = models.CharField(max_length=100)
    description = models.TextField("简评", max_length=200, default="")
    content = MarkdownField("内容")
    publish_time = models.DateTimeField("发表时间", default=timezone.now)
    image = models.ImageField(upload_to="post/%Y/%m/%d", blank=True)
    tags = TaggableManager(help_text="输入逗号分割的标签串", blank=True)

    objects = models.Manager()
    published = PostPublishedManager()

    class Meta:
        ordering = ("-publish_time",)
        verbose_name = verbose_name_plural = "博客文章"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self,
                           max_length=30, start_no=2)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Carousel(TimeStampAbsClass):
    post = models.OneToOneField(Post, verbose_name="文章",
                                on_delete=models.CASCADE)
    index = models.IntegerField("顺序")

    class Meta:
        verbose_name = verbose_name_plural = "轮播图"
        ordering = ("index", )

    def __str__(self):
        return "{} - 轮播图".format(self.post)



