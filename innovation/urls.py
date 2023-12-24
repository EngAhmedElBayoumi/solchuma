#import path
from django.urls import path
#import views
from . import views

app_name = 'innovation'

urlpatterns = [
    #Digital_Transformation , Research_and_Development
    path('en/Digital_Transformation/', views.digital_transformation, name='digital_transformation'),
    path('ar/Digital_Transformation/', views.digital_transformation_ar, name='digital_transformation_ar'),
    path('en/Research_and_Development/', views.research_and_development, name='research_and_development'),
    path('ar/Research_and_Development/', views.research_and_development_ar, name='research_and_development_ar'),
]