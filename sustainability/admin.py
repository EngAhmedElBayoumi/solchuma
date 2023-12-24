from django.contrib import admin
from .models import Envronmental_section_one, Envronmental_section_two, Tab, Tabs, Envronmental, Social_section_one, Social_section_two,files , Social ,Governance_section_one
from .models import Crs_section_one , statistics , Crs_section_two , descriptions ,Crs_section_three , Crs_section_four , Sustainability_reports , Ims_reports , Certifications

# Register your models here.

admin.site.register(Envronmental_section_one)
admin.site.register(Envronmental_section_two)
admin.site.register(Tab)
admin.site.register(Tabs)
admin.site.register(Envronmental)
admin.site.register(Social_section_one)
admin.site.register(Social_section_two)
admin.site.register(files)
admin.site.register(Social)
admin.site.register(Governance_section_one)
admin.site.register(Crs_section_one)
admin.site.register(statistics)
admin.site.register(Crs_section_two)
admin.site.register(descriptions)
admin.site.register(Crs_section_three)
admin.site.register(Crs_section_four)
admin.site.register(Sustainability_reports)
admin.site.register(Ims_reports)
admin.site.register(Certifications)