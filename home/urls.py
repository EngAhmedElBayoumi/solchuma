#import path , views
from django.urls import path
from . import views

app_name = 'home'  # here for namespacing of urls.

urlpatterns = [
    path('', views.home, name='home'),
    path('en/', views.home, name='home_en'),
    path('ar/', views.home_ar, name='home_ar'),
    path('en/policy', views.policy, name='policy'),
    path('ar/policy', views.policy_ar, name='policy_ar'),
]
