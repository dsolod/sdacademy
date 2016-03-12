from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def courses_list(request):
    courses = Course.objects.all()
    return render(request, '../templates/index.html', 
        {'courses_list': courses})


def detail(request, pk):
    
    lessons = Lesson.objects.filter(course=pk)
    course = Course.objects.get(id=pk)
    coache = Coach.objects.get(id=course.coach.id)
    assistant = Coach.objects.get(id=course.assistant.id)
#    print course.coach
    return render(request, '../templates/courses/detail.html', 
            {'courses_list': lessons,
            'pk': pk,
            'course': course,
            'coach': coache,
            'assistant' : assistant})


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