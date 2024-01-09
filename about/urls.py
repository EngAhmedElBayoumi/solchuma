#import path 
from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    #About Sipchem en
    path('en/about_solchema', views.about, name='about_solchema'),
    #About Sipchem ar
    path('ar/about_solchema', views.about_ar, name='about_solchema_ar'),
    #Leadership en
    path('en/leadership', views.leadership, name='leadership'),
    #Leadership ar
    path('ar/leadership', views.leadership_ar, name='leadership_ar'),
    #Affiliates en
    path('en/affiliates', views.affiliates, name='affiliates'),
    #Affiliates ar
    path('ar/affiliates', views.affiliates_ar, name='affiliates_ar'),
]
