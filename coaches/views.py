from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
# Create your views here.
import datetime
from django.contrib import messages

def detail(request, pk):
    
    try:
        coache = Coach.objects.get(id=pk)
        course = Course.objects.filter(coach=pk)
        assist = Course.objects.filter(assistant=pk)
    except:
        coache = ''
        course = ''
        assist = ''
        messages.info(request, ('There are no coache with id = '
            + pk ))


    return render(request, '../templates/coaches/detail.html', 
        {  
            'coache': coache,
            'course': course,
            'assist': assist,
            'pub_date': datetime.date(2015, 04, 1)
                     })


