from django.contrib import admin
from .models import *


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', 'logo_url')


admin.site.register(Skills, SkillsAdmin)
