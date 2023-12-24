from django.shortcuts import render

# Create your views here.
#journalist_Registraion
def journalist_registration(request):
    return render(request, 'journalist_Registraion.html')

def journalist_registration_ar(request):
    return render(request, 'ar/journalist_Registraion.html')