from django.shortcuts import get_object_or_404, render, redirect 
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from students.models import Student
from courses.models import Course
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, Http404
from .forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    paginate_by = 2
    def get_queryset(self):
        try:
            cour = self.request.GET['course_id']
            return Student.objects.filter(courses__in=cour)    
        except:
            return Student.objects.all()
            


class StudentDetailView(DetailView):
    model = Student

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(pk=pk)
        try:
            obj = queryset.get()
            return obj
        except ObjectDoesNotExist:
            messages.info(self.request, ('There are no Student with id = '
            + pk ))
        

'''
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        print Student.objects.get(id=pk)
        try:
            Student.objects.get(id=pk)

        except:
             messages.info(self.request, ('There are no Student with id = '
            + pk ))

        return obj
'''



class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Student ' + self.request.POST['name'] +
             ' ' + self.request.POST['surname'] + ' has been successfully added.')
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list')
     
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        messages.success(self.request, ('Info on the student has'
                            ' been sucessfully changed.'))
        return super(StudentUpdateView, self).form_valid(form)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(pk=pk)
        try:
            obj = queryset.get()
            return obj
        except ObjectDoesNotExist:
            messages.info(self.request, ('There are no Student with id = '
            + pk ))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

    #print pk
    #comment = get_object_or_404(Comment, pk=comment_id)

#    def get_object(self, queryset=None, **kwargs):
#        print '1'
#        obj = get_object_or_404(Student, id=self.kwargs['pk'])
#        print '2'
#        try:
#            obj = super(StudentDeleteView, self).get_object()
#        except:
#                messages.info(self.request, 'There are no student with id '+ self.kwargs['pk'])
#        print obj
#        return obj


    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression' 

        app = Student.objects.get(id=self.kwargs['pk'])
        messages.info(self.request, 'Student ' + app.name + ' ' + app.surname +
                        ' will be deleted.')
        return context

    def delete(self, request, *args, **kwargs):
        app = Student.objects.get(id=self.kwargs['pk'])
        messages.success(self.request, 'Info on ' + app.name + ' ' + app.surname +
         ' has been sucessfully deleted.')
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)



'''
def detail(request, pk):l
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