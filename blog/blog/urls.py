"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap

from post import views as post_views
from post.sitemaps import PostSitemap
from post.feeds import LatestPostFeed
from core import views as core_views

sitemaps = {
    "posts": PostSitemap
}

urlpatterns = [
    url(r"^admin/",
        include("admin_honeypot.urls", namespace="admin_honeypot")),
    url(r'^fake-admin/', admin.site.urls),
    url(r"^$",
        post_views.homepage_view,
        name="homepage"),
    url(r"^query/$",
        post_views.post_search_view,
        name="post_search"),
    url(r"^post/(?P<slug>[\w-]+)/$",
        post_views.post_detail_view,
        name="post_detail"),
    url(r"^tag/(?P<tag_slug>[\w-]+)$",
        cache_page(60 * 60)(post_views.PostListByTag.as_view()),
        name="post_tagged"),
    url(r"^all/$",
        post_views.PostListView.as_view(),
        name="post_list"),

    url(r"^image/(?P<width>\d+)/(?P<height>\d+)/$",
        core_views.placeholder_view,
        name="placeholder"),

    url(r"^markdown/", include("django_markdown.urls")),

    url(r"^sitemap\.xml$", sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"),

    url(r"^feed/$",
        LatestPostFeed(),
        name="post_feed"),

    url(r"^api/",
        include("post.api.urls", namespace="api")),

    url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^silk/', include('silk.urls', namespace='silk'))   # 性能检测
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns