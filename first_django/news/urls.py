from django.urls import path
from . import views

urlpatterns = [ #тут уже отслеживаем ветку после ../news/
    path('', views.news_home, name='news_home'),
    path('create', views.news_home, name='create'),

]
