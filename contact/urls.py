#path
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    #contact en
    path('en/contact', views.Contact, name='contact'),
    #contact ar
    path('ar/contact', views.contact_ar, name='contact_ar'),
]
