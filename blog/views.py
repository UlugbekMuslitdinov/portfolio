from django.shortcuts import render
from django.db.models import Q
from .models import *
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
