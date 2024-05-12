"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from django.contrib.sitemaps import views as sitemap_views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from blog.apis import PostViewSet, CategoryViewSet
from blog.views import IndexView, PostDetailView, CategoryView, TagView, SearchView, AuthorView
from comment.views import CommentView
from config.views import LinkView
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from typeidea.autocomplete import CategoryAutocomplete, TagAutocomplete

from typeidea.custom_site import custom_site

from .settings import base

from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    path('post/<int:post_id>.html', PostDetailView.as_view(), name='post-detail'),
    path('links/', LinkView.as_view(), name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('rss|feed/', LatestPostFeed(), name='rss'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),

    path('super_admin/', admin.site.urls, name='super_admin'),
    path('admin/', custom_site.urls, name='admin'),

    path('category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('api/', include((router.urls, 'api'))),
    path('api/docs/', include_docs_urls(title='typeidea apis')),

    path('sitemap.xml', cache_page(60 * 20, key_prefix='sitemap+cache_')
    (sitemap_views.sitemap), {'sitemaps': {'posts': PostSitemap}}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if base.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
