from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_detail, name='blog_detail'),
    path('blog-list/', views.blog_list, name='blog_list'),
]