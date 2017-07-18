from django.contrib import admin
from django_markdown.admin import AdminMarkdownWidget, MarkdownField

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug",
                    "publish_time", "created", "modified")
    list_filter = ("publish_time", "created", "modified")
    search_fields = ("title", "content", "author")
    exclude = ("slug",)
    formfield_overrides = {MarkdownField: {"widget": AdminMarkdownWidget}}

