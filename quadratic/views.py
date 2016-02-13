# -*- coding: utf-8 -*-


import math
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

def quadratic_results(request):
 

    if 'a' in request.GET:
        a =  request.GET['a']
        text_a =  check_data(a, 'a')
    else:
        text_a = 'коэффициент не определен'


    if 'b' in request.GET:
        b =  request.GET['b']
        text_b =  check_data(b)
    else:
        text_b = 'коэффициент не определен'
    if 'c' in request.GET:
        c =  request.GET['c']
        text_c =  check_data(c)
    else:
        text_c = 'коэффициент не определен'
    print 'text_a ' + str(text_a)     
    print 'text_b ' + str(text_b) 
    print 'text_c ' + str(text_c)
    if (text_a):
        print '!!!'
    if 'a' in request.GET and 'b' in request.GET and 'c' in request.GET:
        if (text_a or text_b or text_c) or a == "0":
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
                text_diskriminant = 'Квадратное уравнение имеет два действительных корня: x1 = '+ str(x1) +', x2 = '+ str(x2)


         
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
    else:
         return render(request, 'results.html', 
            {            

#                'text_error' : 'errrrrrrr',
                'text_a' : text_a,
                'text_b' : text_b,
                'text_c' : text_c,               
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
        


