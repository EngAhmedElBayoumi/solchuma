#import path
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    #products en
    path('en/products', views.products, name='products'),
    #products ar
    path('ar/products', views.products_ar, name='products_ar'),
    #product details en
    path('en/product_details/<int:id>', views.product_details, name='product_details'),
    #product details ar
    path('ar/product_details/<int:id>', views.product_details_ar, name='product_details_ar'),
    #InqueryProduct en
    path('en/inquery_product', views.inquery_product, name='inquery_product'),
    #InqueryProduct ar
    path('ar/inquery_product', views.inquery_product_ar, name='inquery_product_ar'),
    #products_by_category en
    path('en/products_by_category/<int:id>', views.products_by_category, name='products_by_category'),
    #products_by_category ar
    path('ar/products_by_category/<int:id>', views.products_by_category_ar, name='products_by_category_ar'),
  
    
]