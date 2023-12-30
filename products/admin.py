from django.contrib import admin
from .models import Product, Product_specification, Safety_data , images , category , sub_category
# Register your models here.

#product display  title , category , sub_category
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sub_category')
    list_filter = ('category', 'sub_category')
    search_fields = ('title', 'category', 'sub_category')
    ordering = ['title']
    


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_specification)
admin.site.register(Safety_data)
admin.site.register(images)
admin.site.register(category)
admin.site.register(sub_category)
