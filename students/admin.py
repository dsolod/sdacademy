from django.contrib import admin

# Register your models here.
from .models import Student





class StudentAdmin(admin.ModelAdmin):

    list_display = ['fullname',  'email', 'skype']
    search_fields = ['surname','email' ]
    list_filter = ['courses']
#    filter_horizontal = ['name', 'surname']
    fieldsets = [
        ('Personal info'  , {'fields': ['name','surname', 'date_of_birth']}),
        ('Contact info'  , {'fields': ['email','phone', 'address',  'skype']}),
         (None  , {'fields': ['courses']}),
                ]

    filter_horizontal = ("courses",)          
admin.site.register(Student, StudentAdmin)