from django.shortcuts import render
from .models import *


def home(request):
    """Home page for portfolio"""
    return render(request, 'home.html')


def skills(request):
    """Skills page"""
    return render(request, 'skills.html')


def articles_list(request):
    """List of all articles sorted by the date created"""
    artticles = Article.objects.all().order_by('-created_at')
    context = {'articles': artticles}
    return render(request, 'articles.html', context)


def article_detail(request, article_slug):
    """Detail page for every article"""
    article = Article.objects.get(slug=article_slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)