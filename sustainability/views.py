from django.shortcuts import render
from .models import Governance_section_one , Social ,Envronmental
from .models import Crs_section_one , Crs_section_two , Crs_section_three , Crs_section_four , Sustainability_reports 
from .models import Ims_reports , Certifications
# Create your views here.

# 1- ESG 2- CSR 3- IMS Compliance 4- Certifications 5- Sustainability Reports

def esg_environment(request):
    envronmental = Envronmental.objects.all()
    context={
        'envronmental':envronmental
        }
    return render(request, 'ESG_Environment.html',context)

def esg_environment_ar(request):
    envronmental = Envronmental.objects.all()
    context={
        'envronmental':envronmental
        }
    return render(request, 'ar/ESG_Environment.html',context)

def esg_social(request):
    social=Social.objects.all()
    context={
        'social':social
        }
    return render(request, 'ESG_Social.html',context)

def esg_social_ar(request):
    social=Social.objects.all()
    context={
        'social':social
        }
    return render(request, 'ar/ESG_Social.html',context)

def esg_governance(request):
    governace=Governance_section_one.objects.all()
    context={
        'governace':governace
        }
    return render(request, 'ESG_Governence.html',context)

def esg_governance_ar(request):
    governace=Governance_section_one.objects.all()
    context={
        'governace':governace
        }
    return render(request, 'ar/ESG_Governence.html',context)



def csr(request):
    one=Crs_section_one.objects.all()
    two=Crs_section_two.objects.all()
    three=Crs_section_three.objects.all()
    four=Crs_section_four.objects.all()
    context={
        'one':one,
        'two':two,
        'three':three,
        'four':four
        }
    return render(request, 'CSR.html',context)

def csr_ar(request):
    one=Crs_section_one.objects.all()
    two=Crs_section_two.objects.all()
    three=Crs_section_three.objects.all()
    four=Crs_section_four.objects.all()
    context={
        'one':one,
        'two':two,
        'three':three,
        'four':four
        }
    return render(request, 'ar/CSR.html',context)

def sustainability_reports(request):
    reports=Sustainability_reports.objects.all()
    context={
        'reports':reports
        }
    return render(request, 'Sustainability_Reports.html',context)

def sustainability_reports_ar(request):
    reports=Sustainability_reports.objects.all()
    context={
        'reports':reports
        }
    return render(request, 'ar/Sustainability_Reports.html',context)

def ims_compliance(request):
    reports=Ims_reports.objects.all()
    certifications=Certifications.objects.all()
    context={
        'reports':reports,
        'certifications':certifications
        }
    return render(request, 'certifications.html',context)

def ims_compliance_ar(request):
    reports=Ims_reports.objects.all()
    certifications=Certifications.objects.all()
    context={
        'reports':reports,
        'certifications':certifications
        }
    return render(request, 'ar/certifications.html',context)

def certifications(request):
    reports=Ims_reports.objects.all()
    certifications=Certifications.objects.all()
    context={
        'reports':reports,
        'certifications':certifications
        }
    return render(request, 'certifications.html',context)

def certifications_ar(request):
    reports=Ims_reports.objects.all()
    certifications=Certifications.objects.all()
    context={
        'reports':reports,
        'certifications':certifications
        }
    return render(request, 'ar/certifications.html',context)

