from django.contrib import admin

# Register your models here.
from .models import Coach





class CoachAdmin(admin.ModelAdmin):

    list_display = ['first_name',  'last_name', 'gender', 'skype', 'description']
    search_fields = ['surname','email' ]
    list_filter = ['is_staff']
#    filter_horizontal = ['name', 'surname']
       
admin.site.register(Coach)