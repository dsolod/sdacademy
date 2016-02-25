from django.shortcuts import get_object_or_404, render
from django.views import generic
from courses.models import Course, Lesson


'''
class IndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.all()'''

def courses_list(request):
    courses = Course.objects.all()
    return render(request, '../templates/index.html', 
        {  'courses_list': courses })

def detail(request, pk):
    
    lessons = Lesson.objects.filter(course=pk)
    course = Course.objects.get(id=pk)
#    print course
    return render(request, '../templates/courses/detail.html', 
        {  'courses_list': lessons,
            'pk': pk,
            'course': course
         })

'''   
class DetailView(generic.DetailView):
    model = Course
    template_name = '../templates/courses/detail.html'
'''
