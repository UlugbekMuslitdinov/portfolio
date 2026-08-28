from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['blog:home', 'blog:projects', 'blog:skills', 'blog:post_list']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
