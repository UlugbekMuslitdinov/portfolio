from django.db import models
from blog.models import Skills


class Project(models.Model):
    """Project model"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    skills_used = models.ManyToManyField(Skills)

    def __str__(self):
        return self.title

    def skills_used_list(self):
        return [{'name': skill.skill, 'logo_url': skill.logo_url} for skill in self.skills_used.all()]
