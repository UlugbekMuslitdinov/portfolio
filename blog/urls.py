from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('blog/', post_list, name='post_list'),
    path('blog/<slug:slug>/', post_detail, name='post_detail'),
    path('', home, name='home'),
]
