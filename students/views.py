from django.shortcuts import get_object_or_404, render
from django.views import generic
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = '../templates/students/list.html'
    context_object_name = 'students_list'
    

    def get_queryset(self):
        
        try:
            cour= self.request.GET['course_id']
            return Student.objects.filter(courses__in=cour)
        except:
    #    self.student = get_object_or_404(Student, id=self.args[0])
        
            return Student.objects.all()





class DetailView(generic.DetailView):
    model = Student
    template_name = '../templates/students/detail.html'




