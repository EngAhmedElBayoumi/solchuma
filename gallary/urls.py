from django.urls import path
from . import views

app_name = 'gallary'

urlpatterns = [
    path('en/gallary', views.gallary, name='gallary'),
    path('ar/gallary', views.gallary_ar, name='gallary_ar'),
    path('en/gallary_details/<int:id>', views.gallary_details, name='gallary_details'),
    path('ar/gallary_details/<int:id>', views.gallary_details_ar, name='gallary_details_ar'),
]
