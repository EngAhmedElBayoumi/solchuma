from django.contrib import admin
from .models import section_one, section_two, section_three, section_four, section_five , affiliates , investments , management_team ,board_of_directors 

# Register your models here.

admin.site.register(section_one)
admin.site.register(section_two)
admin.site.register(section_three)
admin.site.register(section_four)
admin.site.register(section_five)
admin.site.register(affiliates)
admin.site.register(investments)
admin.site.register(management_team)
admin.site.register(board_of_directors)
