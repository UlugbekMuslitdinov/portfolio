from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['blog:home', 'blog:projects', 'blog:skills', 'blog:articles_list', 'blog:search_results']

    def location(self, item):
        return reverse(item)