from django.contrib import admin


# Register your models here.
# admin.py

from django.contrib import admin
from .models import Banner, Sipchem, Investors, Sustainability, Careers , Products

admin.site.register(Banner)
admin.site.register(Sipchem)
admin.site.register(Investors)
admin.site.register(Products)
admin.site.register(Sustainability)
admin.site.register(Careers)
