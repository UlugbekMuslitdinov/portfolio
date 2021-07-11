from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("topic",)}
    list_display = ('topic', 'author', 'created_at')

admin.site.register(Article, ArticleAdmin)