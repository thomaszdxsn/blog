from django.shortcuts import render

from .models import Post


def homepage_view(request):
    posts = Post.published.all()
    return render(request, "post/index.html",
                  {"posts": posts})