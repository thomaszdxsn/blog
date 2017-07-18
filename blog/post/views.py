from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Post


def homepage_view(request):
    posts = Post.published.all()
    return render(request, "post/index.html",
                  {"posts": posts})


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/detail.html",
                  {"post": post})


def post_search_view(request):
    query = request.GET.get("query", "")
    posts = None
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, "post/search.html",
                  {"posts": posts, "query": query})