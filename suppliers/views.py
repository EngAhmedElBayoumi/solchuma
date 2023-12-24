from django.shortcuts import render
from .models import Section_one , Section_two

# Create your views here.

def subliers(request):
    one=Section_one.objects.all()
    two=Section_two.objects.all()
    context={
        'one':one,
        'two':two
    }
    return render(request, 'sublier.html',context)


def subliers_ar(request):
    one=Section_one.objects.all()
    two=Section_two.objects.all()
    context={
        'one':one,
        'two':two
    }
    return render(request, 'ar/sublier.html',context)