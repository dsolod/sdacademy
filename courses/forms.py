# -*- coding: utf-8 -*-


from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ()
        #fields = '__all__'


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ()
#        fields = ['subject', 'description', 'course', 'order']

        