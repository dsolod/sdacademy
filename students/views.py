from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import StudentModelForm
from django.contrib import messages
'''
class IndexView(generic.ListView):
    template_name = '../templates/students/list.html'
    context_object_name = 'students_list'
    def get_queryset(self):
        try:
            cour= self.request.GET['course_id']
            return Student.objects.filter(courses__in=cour)
        except:

            return Student.objects.all()
'''


def list(request):
    try:
        cour = request.GET['course_id']
        students = Student.objects.filter(courses__in=cour)
    except:
        students = Student.objects.all()
    return render(request, '../templates/students/list.html', 
        {'students_list': students})


def detail(request, pk):
    students = Student.objects.get(id=pk)
    return render(request, '../templates/students/detail.html', 
        {'student': students})


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        #print request.POST
        if form.is_valid():

            data = form.cleaned_data
            messages.success(request, 'Student ' + data['name'] +
             ' ' + data['surname'] + ' has been successfully added.')
            form.save()
            return redirect('students:list')
    else:
        form = StudentModelForm()
        return render(request, '../templates/students/add.html', 
        {'form': form})

            


def edit(request, pk):
    app = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=app)
        if form.is_valid():

            messages.success(request, 'Info on the student has been sucessfully changed.')
            app = form.save()
    else:
        form = StudentModelForm(instance=app)

    return render(request, '../templates/students/edit.html', {'form': form})


def remove(request, pk):
    app = Student.objects.get(id=pk)
    messages.info(request, 'Student ' + app.name + ' ' + app.surname +
     ' will be deleted.')
    if request.method == "POST":
        messages.success(request, 'Info on ' + app.name + ' ' + app.surname +
         ' has been sucessfully deleted.')

        app.delete()
        return redirect('students:list')
    else:
        return render(request, '../templates/students/remove.html', {'app': app})


'''
class DetailView(generic.DetailView):
    model = Student
    template_name = '../templates/students/detail.html'
'''


