from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blogApp.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

    # def location(self, item):
    #   return reverse("blog:blog-single", kwargs={"pid": item.id})
