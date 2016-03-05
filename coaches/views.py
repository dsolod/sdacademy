from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
# Create your views here.
import datetime

def detail(request, pk):
    
    
    coache = Coach.objects.get(id=pk)
    course = Course.objects.filter(coach=pk)
    assist = Course.objects.filter(assistant=pk)
#    print assist,pk
#    print course.coach
    return render(request, '../templates/coaches/detail.html', 
        {  
            'coache': coache,
            'course': course,
            'assist': assist,
            'pub_date': datetime.date(2015, 04, 1)
                     })
