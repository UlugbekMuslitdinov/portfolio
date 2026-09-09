from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    """Blog post. Body is written in Markdown and rendered on the frontend."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    body = models.TextField(help_text='Markdown formatted content')
    cover_image = models.ImageField(
        upload_to='blog/covers/',
        blank=True,
        null=True,
        help_text='Optional. Shown at the top of the post and as a thumbnail in the blog list.'
    )
    tags = models.CharField(
        max_length=250,
        blank=True,
        help_text='Comma separated keywords, e.g. python, django, web'
    )
    excerpt = models.CharField(
        max_length=300,
        blank=True,
        help_text='Short summary used for list previews and SEO description. Leave empty to auto-generate.'
    )
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    @property
    def tag_list(self):
        """Return tags as a list of strings."""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    @property
    def description(self):
        """Plain-text description used for SEO meta tags and previews."""
        if self.excerpt:
            return self.excerpt
        plain = ' '.join(self.body.replace('#', ' ').replace('`', ' ')
                         .replace('*', ' ').replace('_', ' ').replace('[', ' ').replace(']', ' ')
                         .split())
        return (plain[:250] + '...') if len(plain) > 250 else plain


class Skills(models.Model):
    skill = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.skill[:50]

    def get_absolute_url(self):
        return reverse('blog:skills_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Skills'
