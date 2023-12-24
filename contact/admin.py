from django.contrib import admin
from .models import Country_code, Message_type, contact, contact_message
# Register your models here.
admin.site.register(Country_code)
admin.site.register(Message_type)
admin.site.register(contact)
admin.site.register(contact_message)
