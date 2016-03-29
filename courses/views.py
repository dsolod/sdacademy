from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def courses_list(request):
    courses = Course.objects.all()
    return render(request, '../templates/index.html', 
        {'courses_list': courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = '../templates/courses/detail.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course__in=pk)
        context['coach'] = Coach.objects.get(id=Course.objects.get(id=pk).coach.id)
        context['assistant'] = Coach.objects.get(id=Course.objects.get(id=pk).assistant.id)
        context['pk'] = pk
        
        return context


'''
def detail(request, pk):
    
    lessons = Lesson.objects.filter(course=pk)
    course = Course.objects.get(id=pk)
    context = {'pk': pk}
    context['courses_list'] = lessons
    context['course'] = course
    try:
        context['coach'] = Coach.objects.get(id=course.coach.id)
    except:
        pass
    try:
        context['assistant'] = Coach.objects.get(id=course.assistant.id)
    except:
        pass
    print context
    return render(request, '../templates/courses/detail.html',  context)
#            {'courses_list': lessons,
#            'pk': pk,
#            'course': course,
#            'coach': coache,
#            'assistant' : assistant})


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        print request.POST
        if form.is_valid():

            data = form.cleaned_data
            messages.success(request, 'Course ' + data['name'] +
             ' has been successfully added.')
            form.save()
            return HttpResponseRedirect(reverse('index'))

       
        else:
            form = CourseModelForm(request.POST)

    else:
        form = CourseModelForm()
    
    return render(request, '../templates/courses/add.html', 
        {'form': form})
'''
class CourseCreateView(CreateView):
    model = Course
    template_name = '../templates/courses/add.html'
    context_object_name = 'courses_list'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Course ' + self.request.POST['name'] +
              ' has been successfully added.')
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = '../templates/courses/edit.html'
    fields = '__all__'
    #def get_object(self):
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        #print self.request.POST
        messages.success(self.request, ('The changes have been saved.'))
        return super(CourseUpdateView, self).form_valid(form)

'''     
def edit(request, pk):
    try:
        app = Course.objects.get(id=pk)
        if request.method == "POST":
            form = CourseModelForm(request.POST, instance=app)
            if form.is_valid():
                messages.success(request, 'The changes have been saved.')
                app = form.save()
                return HttpResponseRedirect(reverse('courses:edit', 
                    args=(pk, )))
            else:
                form = CourseModelForm(request.POST, instance=app)
        else:
            form = CourseModelForm(instance=app)

        return render(request, '../templates/courses/edit.html', {'form': form})
    except:
        messages.success(request, 'Provided id ' + pk + ' does not exist.')
        return HttpResponseRedirect(reverse('index'))


def remove(request, pk):
    try:
        app = Course.objects.get(id=pk)
        messages.success(request, 'Course ' + app.name + ' will be deleted.')
        if request.method == "POST":
            messages.success(request, 'Course ' + app.name + ' has been deleted.')
            app.delete()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, '../templates/courses/remove.html', 
                {'app': app})
    except:
        messages.success(request, 'Provided id ' + pk + ' does not exist.')
        return HttpResponseRedirect(reverse('index'))
'''

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = '../templates/courses/remove.html'
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        app = Course.objects.get(id=self.kwargs['pk'])
        messages.info(self.request, 'Course ' + app.name + 
                        ' will be deleted.')
        return context

    def delete(self, request, *args, **kwargs):
        app = Course.objects.get(id=self.kwargs['pk'])
        messages.success(self.request, 'Course ' + app.name +
         ' has been sucessfully deleted.')
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


class LessonCreateView(CreateView):
    model = Lesson
    template_name = '../templates/courses/add_lesson.html'
    #context_object_name = 'courses_list'
    #success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Lesson creation'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Lesson ' + self.request.POST['subject'] +
              ' has been successfully added.')
        return super(LessonCreateView, self).form_valid(form)

def add_lesson(request, pk):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            messages.success(request, 'Lesson ' + data['subject'] +
             ' has been successfully added.')
            course_app = Course.objects.get(name=data['course'])

            form.save()
            #return redirect('courses:detail', course_app.id )
            #return render(request,
            return HttpResponseRedirect(reverse('courses:detail', args=(course_app.id, )))

        else:
            form = LessonModelForm(request.POST)
    else:
        form = LessonModelForm(initial={'course': pk})
    return render(request, '../templates/courses/add_lesson.html', 
        {'form': form})