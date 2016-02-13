# -*- coding: utf-8 -*-


import math
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

def quadratic_results(request):
    a =  request.GET['a']
    b =  request.GET['b']
    c =  request.GET['c']
    
    text_a =  check_data(a, 'a')
    text_b =  check_data(b)
    text_c =  check_data(c)
    #print int(a)
    #for let in [a,b,c]:
    #   print let
    if text_a:
        print text_a
    #print text_b
    #print text_c
    if (text_a and text_b and text_c) or int(a) == 0:
        diskriminant = ""
        text_diskriminant = ""
    else:
        b = int(b)
        a = int(a) 
        c = int(c)
        diskriminant = b*b - 4*a*c
        if diskriminant < 0:
            text_diskriminant = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        if diskriminant == 0:
            x = -b/(2.0*a)
            text_diskriminant = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
        if diskriminant > 0:
            x1 = (-b + math.sqrt(diskriminant))/(2.0*a)
            x2 = (-b - math.sqrt(diskriminant))/(2.0*a)
            text_diskriminant = 'Квадратное уравнение имеет два действительных корня: x1 = '+ str(x1) +' x2 = '+ str(x2)


         
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
    
    if num:
        #print a
        if num.isdigit() and a =="":
            pass
        elif a == 'a' and num == "0":
            return 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        elif num.lstrip('-').isdigit():
            pass
        else:
            return 'коэффициент не целое число'
    else:
        return 'коэффициент не определен'
        


