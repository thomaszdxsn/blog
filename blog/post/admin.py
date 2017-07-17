from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug",
                    "publish_time", "created", "modified")
    list_filter = ("publish_time", "created", "modified")
    search_fields = ("title", "content", "author")
    exclude = ("slug",)
