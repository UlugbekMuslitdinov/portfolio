from django.urls import path
from .views import *
app_name = 'blog'

urlpatterns = [
    path('blog/<str:article_slug>/', article_detail, name='article_detail'),
    path('blog/', articles_list, name='articles_list'),
    path('skills/', skills, name='skills'),
    path('', home, name='home'),
]