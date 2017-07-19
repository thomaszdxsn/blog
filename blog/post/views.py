from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.views.generic import ListView

from taggit.models import Tag

from .models import Post, Carousel


def homepage_view(request):
    posts = Post.published.all()[:20]
    carousel_posts = Carousel.objects.all()[:3]
    tags = Tag.objects.all()[:15]
    return render(request, "post/index.html",
                  {"posts": posts, "carousel_posts": carousel_posts, "tags": tags})


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_tags_id = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_id).exclude(id=post.id)
    similar_posts = (similar_posts.annotate(same_tags=Count("tags"))
                                  .order_by("-same_tags", "-publish_time"))[:4]
    return render(request, "post/detail.html",
                  {"post": post, "similar_posts": similar_posts})


def post_search_view(request):
    query = request.GET.get("query", "")
    posts = None
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, "post/search.html",
                  {"posts": posts, "query": query})


def post_list_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, "post/tagged.html",
                  {"posts": posts, "tag": tag})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = "post/list.html"

    def get_context_data(self, **kwargs):
        data = super(PostListView, self).get_context_data()
        data["section"] = "all"
        print("data", data)
        return data

