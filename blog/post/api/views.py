#!/usr/bin/env python3
from rest_framework import viewsets

from .serializers import PostSerializer
from ..models import Post


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer

