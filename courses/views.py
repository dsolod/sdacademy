from django.shortcuts import get_object_or_404, render
from django.views import generic

from courses.models import Course, Lesson


#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse


class IndexView(generic.ListView):
    template_name = '../templates/index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        """Return the last five published questions."""
#        print Course.objects.all()
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = '../templates/courses/detail.html'

#    def get_context_data(self, **kwargs):
#        print self.request.GET
    # Call the base implementation first to get a context
#        context = super(Course, self).get_context_data(**kwargs)
    # Add in the publisher
#        context['course_id'] = self.idd
#        return context