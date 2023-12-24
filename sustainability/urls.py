#import path
from django.urls import path
from . import views

app_name = 'sustainability'

urlpatterns = [
  #1 esg_environment en
    path('en/esg_environment', views.esg_environment, name='esg_environment'),
    #1 esg_environment ar
    path('ar/esg_environment', views.esg_environment_ar, name='esg_environment_ar'),
    #2 esg_social en
    path('en/esg_social', views.esg_social, name='esg_social'),
    #2 esg_social ar
    path('ar/esg_social', views.esg_social_ar, name='esg_social_ar'),
    #3 esg_governance en
    path('en/esg_governance', views.esg_governance, name='esg_governance'),
    #3 esg_governance ar
    path('ar/esg_governance', views.esg_governance_ar, name='esg_governance_ar'),
    #4 csr en
    path('en/csr', views.csr, name='csr'),
    #4 csr ar
    path('ar/csr', views.csr_ar, name='csr_ar'),
    #5 ims_compliance en
    path('en/ims_compliance', views.ims_compliance, name='ims_compliance'),
    #5 ims_compliance ar
    path('ar/ims_compliance', views.ims_compliance_ar, name='ims_compliance_ar'),
    #6 certifications en
    path('en/certifications', views.certifications, name='certifications'),
    #6 certifications ar
    path('ar/certifications', views.certifications_ar, name='certifications_ar'),
    #7 sustainability_reports en
    path('en/sustainability_reports', views.sustainability_reports, name='sustainability_reports'),
    #7 sustainability_reports ar
    path('ar/sustainability_reports', views.sustainability_reports_ar, name='sustainability_reports_ar'),
]