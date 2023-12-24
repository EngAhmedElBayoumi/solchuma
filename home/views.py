from django.shortcuts import render
from .models import Banner, Sipchem, Investors, Sustainability, Careers , Products


# Create your views here.

def home(request):
    #banner
    banner = Banner.objects.all()
    #sipchem
    sipchem = Sipchem.objects.all()
    #investors
    investors = Investors.objects.all()
    #sustainability
    sustainability = Sustainability.objects.all()
    #careers
    careers = Careers.objects.all()
    #products
    products = Products.objects.all()
    context = {
        'banner':banner,
        'sipchem':sipchem,
        'investors':investors,
        'sustainability':sustainability,
        'careers':careers,
        'products':products,
    }
    return render(request,'index.html',context)

def home_ar(request):
    #banner
    banner = Banner.objects.all()
    #sipchem
    sipchem = Sipchem.objects.all()
    #investors
    investors = Investors.objects.all()
    #sustainability
    sustainability = Sustainability.objects.all()
    #careers
    careers = Careers.objects.all()
    #products
    products = Products.objects.all()
    context = {
        'banner':banner,
        'sipchem':sipchem,
        'investors':investors,
        'sustainability':sustainability,
        'careers':careers,
        'products':products,
    }
    return render(request,'ar/index.html',context)

#Policy
def policy(request):
    return render(request,'Policy.html')

def policy_ar(request):
    return render(request,'ar/Policy.html')