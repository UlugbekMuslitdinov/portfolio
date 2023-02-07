from django.shortcuts import render
from .models import *


def projects(request):
    """Projects page"""
    projects_list = Project.objects.all()
    context = {'projects_list': projects_list}
    return render(request, 'projects.html', context)
