#!/usr/bin/env python3
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars

from .models import Post


class LatestPostFeed(Feed):
    title = "zdxsn's blog"
    link = "/post/"
    description = "zdxsn's blog的新文章"

    def items(self):
        return Post.published.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatechars(item.description, 120)