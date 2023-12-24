#path
from django.urls import path
from . import views

app_name = 'suppliers'

urlpatterns = [
    #subliers en
    path('en/subliers', views.subliers, name='subliers'),
    #subliers ar
    path('ar/subliers', views.subliers_ar, name='subliers_ar'),
]