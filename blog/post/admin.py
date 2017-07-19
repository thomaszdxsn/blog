from django.contrib import admin
from django_markdown.admin import AdminMarkdownWidget, MarkdownField

from .models import Post, Carousel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author","publish_time",
                    "created", "modified")
    list_filter = ("publish_time", "created", "modified")
    search_fields = ("title", "content", "author")
    exclude = ("slug",)
    formfield_overrides = {MarkdownField: {"widget": AdminMarkdownWidget}}


@admin.register(Carousel)
class Carousel(admin.ModelAdmin):
    list_display = ("post", "index")
    raw_id_fields = ("post",)
