from django.shortcuts import render, get_object_or_404
from .models import Skills, Post
from projects.models import Project


def home(request):
    """Home page for portfolio"""
    skills_list = Skills.objects.all()
    context = {'skills_list': skills_list}
    return render(request, 'home.html', context)


def skills(request):
    """Skills page"""
    skills = Skills.objects.all()
    context = {'skills': skills}
    return render(request, 'skills.html', context)


def projects(request):
    """My projects list"""
    project_list = Project.objects.all()
    context = {'projects': project_list}
    return render(request, 'projects.html', context)


def post_list(request):
    """Blog posts sorted from newest to oldest"""
    posts = Post.objects.filter(published=True)
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    """Single blog post rendered from Markdown"""
    post = get_object_or_404(Post, slug=slug, published=True)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
