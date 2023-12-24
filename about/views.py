from django.shortcuts import render
from .models import section_one as Section_one , section_two as Section_two, section_three as Section_three, section_four as Section_four, section_five as Section_five , affiliates as Affiliates , investments  as  Investments, management_team ,board_of_directors


# Create your views here.

def about(request):
    # all sections
    section_one = Section_one.objects.all()
    section_two = Section_two.objects.all()
    section_three = Section_three.objects.all()
    section_four = Section_four.objects.all()
    section_five = Section_five.objects.all()
    context={
        'section_one': section_one,
        'section_two': section_two,
        'section_three': section_three,
        'section_four': section_four,
        'section_five': section_five,
    }
    
    return render(request, 'About.html', context)

def about_ar(request):
    # all sections
    section_one = Section_one.objects.all()
    section_two = Section_two.objects.all()
    section_three = Section_three.objects.all()
    section_four = Section_four.objects.all()
    section_five = Section_five.objects.all()
    context={
        'section_one': section_one,
        'section_two': section_two,
        'section_three': section_three,
        'section_four': section_four,
        'section_five': section_five,
    }
    return render(request, 'ar/About.html', context)

def leadership(request):
    Management_team = management_team.objects.all()
    Board_of_directors = board_of_directors.objects.all()
    
    context={
        'Management_team': Management_team,
        'Board_of_directors': Board_of_directors,
    }
    return render(request, 'leadershep.html', context)

def leadership_ar(request):
    Management_team = management_team.objects.all()
    Board_of_directors = board_of_directors.objects.all()
    
    context={
        'Management_team': Management_team,
        'Board_of_directors': Board_of_directors,
    }
    return render(request, 'ar/leadershep.html', context)

def affiliates(request):
    affiliates = Affiliates.objects.all()
    investments = Investments.objects.all()
    context={
        'affiliates': affiliates,
        'investments': investments,
    }
    return render(request, 'Afilities.html', context)

def affiliates_ar(request):
    affiliates = Affiliates.objects.all()
    investments = Investments.objects.all()
    context={
        'affiliates': affiliates,
        'investments': investments,
    }
    return render(request, 'ar/Afilities.html', context)

