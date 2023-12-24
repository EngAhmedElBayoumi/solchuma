#path
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('en/news', views.news, name='news'),
    path('ar/news', views.news_ar, name='news_ar'),
    path('en/news_details/<int:id>', views.news_details, name='news_details'),
    path('ar/news_details/<int:id>', views.news_details_ar, name='news_details_ar'),
]