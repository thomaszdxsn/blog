#!/usr/bin/env python3
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^$", views.homepage_view, name="homepage"),
]