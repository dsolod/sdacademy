#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')


