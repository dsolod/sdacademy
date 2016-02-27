from django.contrib import admin
from .models import Course, Lesson



class LessonInline(admin.TabularInline):
    model = Lesson

    fieldsets = [
        (None,               {'fields': [('subject', 'description', 'order')]}),
    #                'description': ['subject', 'description', 'order'],
                ]

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','short_description']
    search_fields = ['name']
    inlines = [LessonInline]
    fieldsets = [
        (None  ,            {'fields': ['name','short_description', 'description']}),
  
                ]
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)