#import path 
from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    #About Sipchem en
    path('en/about_sipchem', views.about, name='about_sipchem'),
    #About Sipchem ar
    path('ar/about_sipchem', views.about_ar, name='about_sipchem_ar'),
    #Leadership en
    path('en/leadership', views.leadership, name='leadership'),
    #Leadership ar
    path('ar/leadership', views.leadership_ar, name='leadership_ar'),
    #Affiliates en
    path('en/affiliates', views.affiliates, name='affiliates'),
    #Affiliates ar
    path('ar/affiliates', views.affiliates_ar, name='affiliates_ar'),
]
