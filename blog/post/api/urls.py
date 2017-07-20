#!/usr/bin/env python3
from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    url('^', include(router.urls))
]