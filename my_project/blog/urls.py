

from . import views

from django.urls import path,re_path


urlpatterns = [
   
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('post/<int:post_id>/', views.post_detail, name='post_detail'),
   path('user/<str:username>/', views.user_profile, name='user_profile'),

   path('article/<int:year>/<int:month>/<int:day>/', views.article_detail, name='article_detail'),

   re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_year, name='article_year'),
    
]