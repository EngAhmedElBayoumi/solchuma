from django.shortcuts import render

# Create your views here.

#Gallary
def gallary(request):
    return render(request, 'Gallary.html')

def gallary_ar(request):
    return render(request, 'ar/Gallary.html')

#Gallary_Details

def gallary_details(request,id):
    return render(request, 'Gallary_Details.html')

def gallary_details_ar(request,id):
    return render(request, 'ar/Gallary_Details.html')

    