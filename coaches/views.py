from django.shortcuts import render
from coaches.models import Coach

# Create your views here.


def detail(request, pk):
    
    
    coache = Coach.objects.get(id=pk)
#    print course.coach
    return render(request, '../templates/coaches/detail.html', 
        {  
            'coache': coache,

         })
