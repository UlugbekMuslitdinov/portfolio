from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("topic",)}
    list_display = ('topic', 'author', 'created_at')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', 'logo_url')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Skills, SkillsAdmin)
