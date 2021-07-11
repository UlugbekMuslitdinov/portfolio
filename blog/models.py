from django.db import models
from django.urls import reverse

class Article(models.Model):
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    summary = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic[:50]

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.slug)])