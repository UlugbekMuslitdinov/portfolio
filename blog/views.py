from django.shortcuts import render
from django.db.models import Q
from .models import *


def home(request):
    """Home page for portfolio"""
    return render(request, 'home.html')


def skills(request):
    """Skills page"""
    return render(request, 'skills.html')


def projects(request):
    """My projects list"""
    return render(request, 'projects.html')


def articles_list(request):
    """List of all articles sorted by the date created"""
    articles = Article.objects.all().order_by('-created_at')
    context = {'articles': articles}
    return render(request, 'articles.html', context)


def article_detail(request, article_slug):
    """Detail page for every article"""
    article = Article.objects.get(slug=article_slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

def search_results(request):
    query = request.GET.get('q')
    object_list = Article.objects.filter(
        Q(topic__icontains=query) | Q(text__icontains=query) | Q(summary__icontains=query) | Q(author__icontains=query)
    )
    context = {'object_list': object_list}
    return render(request, 'search_results.html', context)