from django.contrib import admin
from .models import *
from blog.models import Skills


class SkillsInline(admin.TabularInline):
    model = Project.skills_used.through
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'url', 'source_code')
    inlines = [SkillsInline]


admin.site.register(Project, ProjectAdmin)
