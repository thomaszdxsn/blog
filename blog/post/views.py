from django.shortcuts import render, get_object_or_404

from .models import Post


def homepage_view(request):
    posts = Post.published.all()
    return render(request, "post/index.html",
                  {"posts": posts})


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/detail.html",
                  {"post": post})