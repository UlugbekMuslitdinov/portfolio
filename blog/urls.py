from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('', home, name='home'),
]