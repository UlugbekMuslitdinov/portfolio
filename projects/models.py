from django.db import models
from blog.models import Skills


class ProjectType(models.Model):
    """Project Type Model"""
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    image = models.TextField()

    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    """Project model"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    skills_used = models.ManyToManyField(Skills)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
