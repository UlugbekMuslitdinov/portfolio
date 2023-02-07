from django.db import models
from django.urls import reverse


class Skills(models.Model):
    skill = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.skill[:50]

    def get_absolute_url(self):
        return reverse('blog:skills_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Skills'
