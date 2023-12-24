from django.contrib import admin
from .models import Product, Product_specification, Safety_data , images , category , sub_category
# Register your models here.
admin.site.register(Product)
admin.site.register(Product_specification)
admin.site.register(Safety_data)
admin.site.register(images)
admin.site.register(category)
admin.site.register(sub_category)
