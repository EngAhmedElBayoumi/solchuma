from django.urls import path
from . import views

app_name = 'journalist'

urlpatterns = [
    path('en/journalist_registration', views.journalist_registration, name='journalist_registration'),
    path('ar/journalist_registration', views.journalist_registration_ar, name='journalist_registration_ar'),
]