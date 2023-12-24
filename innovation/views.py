from django.shortcuts import render
from .models import Digital_transformation , Research_and_development
 
# Create your views here.

# Digital_Transformation , Research_and_Development
def digital_transformation(request):
    content=Digital_transformation.objects.all()
    context={'content':content}
    return render(request, 'Digital_Transformation.html',context)

def digital_transformation_ar(request):
    content=Digital_transformation.objects.all()
    context={'content':content}
    return render(request, 'ar/Digital_Transformation.html', context)

def research_and_development(request):
    research=Research_and_development.objects.all()
    context={'research':research}
    return render(request, 'Research_and_Development.html', context)

def research_and_development_ar(request):
    research=Research_and_development.objects.all()
    context={'research':research}
    return render(request, 'ar/Research_and_Development.html', context)

