from django.shortcuts import render
from .models import Product, Product_specification, Safety_data , images , category , sub_category as SubCategory
import json
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.db.models import Count

# Create your views here.

#caterories




def products(request):
    products_data = Product.objects.all()
    category_data = category.objects.all()
    context={
        'products':products_data,
        'category':category_data
    }
    
    return render(request, 'Products.html', context)

#get products by category id
def products_by_category(request, id):
     # Get distinct subcategories for the given category
    subcategories = SubCategory.objects.filter(product__category=id).distinct()

    # Get all products for the category
    products_data = Product.objects.filter(category=id)

    context = {
        'subcategories': subcategories,
        'products': products_data,
    }  
    return render(request, 'Products.html', context)

#arabic
def products_by_category_ar(request, id):
     # Get distinct subcategories for the given category
    subcategories = SubCategory.objects.filter(product__category=id).distinct()

    # Get all products for the category
    products_data = Product.objects.filter(category=id)

    context = {
        'subcategories': subcategories,
        'products': products_data,
    }  
    return render(request, 'ar/Products.html', context)






def products_ar(request):
    products_data = Product.objects.all()
    category_data = category.objects.all()
    context={
        'products':products_data,
        'category':category_data
    }
    return render(request, 'ar/Products.html', context)

def product_details(request, id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    return render(request, 'Products_Details.html', context)

def product_details_ar(request, id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    return render(request, 'ar/Products_Details.html', context)

def inquery_product(request):
    return render(request, 'InqueryProduct.html')

def inquery_product_ar(request):
    return render(request, 'ar/InqueryProduct.html')