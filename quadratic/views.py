# -*- coding: utf-8 -*-


import math
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

def quadratic_results(request):

    answers = ('Дискриминант меньше нуля, квадратное уравнение не \
        имеет действительных решений.', 'Дискриминант равен нулю, квадратное \
        уравнение имеет один действительный корень: x1 = x2 = ', 'Квадратное \
        уравнение имеет два действительных корня: x1 = ')
    a = request.GET.get("a", '')
    b = request.GET.get("b", '')
    c = request.GET.get("c", '')
    text_a =  check_data(a, 'a')
    text_b =  check_data(b)
    text_c =  check_data(c)
    diskriminant = ""
    text_diskriminant = ""

    if not text_a and not text_b and not text_c:

        b = int(b)
        a = int(a) 
        c = int(c)
        diskriminant = b*b - 4*a*c
        if diskriminant < 0:
            text_diskriminant = answers[0]
        if diskriminant == 0:
            x = -b/(2.0*a)
            text_diskriminant = answers[1] + str(x)
        if diskriminant > 0:
            x1 = (-b + math.sqrt(diskriminant))/(2.0*a)
            x2 = (-b - math.sqrt(diskriminant))/(2.0*a)
            text_diskriminant = answers[2]+ str(x1) +', x2 = '+ str(x2)



    return render(request, 'results.html', 
        {
                'a' : a,
                'b' : b,
                'c' : c,
                'text_a' : text_a,
                'text_b' : text_b,
                'text_c' : text_c,
                'diskriminant' : diskriminant,
                'text_diskriminant' : text_diskriminant,
        })



def check_data(num , a="" ):
    answers = ('коэффициент при первом слагаемом уравнения не \
        может быть равным нулю','коэффициент не целое число',\
        'коэффициент не определен')
    if num:
        #print a
        if num.isdigit() and a =="":
            pass
        elif a == 'a' and num == "0":
            return answers[0]
        elif num.lstrip('-').isdigit():
            pass
        else:
            return answers[1]
    else:
        return answers[2]


