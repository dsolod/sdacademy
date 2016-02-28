from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Coach

class CoachInline(admin.StackedInline):
    model = Coach





class CoachAdmin(admin.ModelAdmin):
    coache = Coach.objects.all()
#    inlines = (CoachInline, )
    list_display = [ 'first_name', 'last_name',   'gender', 'skype', 'description']
    search_fields = ['surname','email' ]
    list_filter = ('user__is_staff',)
#    filter_horizontal = ['name', 'surname']
    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name

#    def is_staff(self, obj):
#        return obj.user.is_staff        
 #   profile_foo.short_description  = 'last_name'


admin.site.register(Coach , CoachAdmin)