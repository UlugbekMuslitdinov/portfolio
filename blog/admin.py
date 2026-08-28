from django.contrib import admin
from .models import *


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', 'logo_url')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'body', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body')
        }),
        ('Meta', {
            'fields': ('tags', 'excerpt', 'published'),
            'description': 'Tags are comma separated keywords used for SEO. '
                           'Excerpt is used as the SEO description and list preview.'
        }),
    )


admin.site.register(Skills, SkillsAdmin)
admin.site.register(Post, PostAdmin)
