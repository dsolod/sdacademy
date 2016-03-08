# -*- coding: utf-8 -*-


import math
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from .form import QuadraticForm

def quadratic_results(request):
    
    context = {}
    answers = ('Дискриминант меньше нуля, квадратное уравнение не \
        имеет действительных решений.', 'Дискриминант равен нулю, квадратное \
        уравнение имеет один действительный корень: x1 = x2 = ', 'Квадратное \
        уравнение имеет два действительных корня: x1 = ')


    diskriminant = ""
    text_diskriminant = ""
    if request.method == 'GET' and request.GET:

        form = QuadraticForm(request.GET)
        
        if form.is_valid():
            print form.clean_a()

            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']


            diskriminant = b*b - 4*a*c
            if diskriminant < 0:
                text_diskriminant = answers[0]
            if diskriminant == 0:
                x = -b/(2.0*a)
                text_diskriminant = answers[1] + str(round(x, 1))
            if diskriminant > 0:
                x1 = (-b + math.sqrt(diskriminant))/(2.0*a)
                x2 = (-b - math.sqrt(diskriminant))/(2.0*a)
                text_diskriminant = answers[2]+ str(round(x1, 1)) +', x2 = '+ str(round(x2, 1))

    else:
        form = QuadraticForm()


    return render(request, 'quadratic/results.html', 
        {


                'diskriminant' : diskriminant,
                'text_diskriminant' : text_diskriminant,
                'form' : form
        })


