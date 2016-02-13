from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from sdacademy import views
from django.conf.urls.static import static
#from views import contact, student_list, index, student_detail

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/results/', include('quadratic.urls', namespace="quadratic")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sdacademy.views.index',name='index'),
    url(r'^index/', 'sdacademy.views.index',name='index'),
    url(r'^contact/', 'sdacademy.views.contact', name='contact'),
    url(r'^student_list/', 'sdacademy.views.student_list', name='student_list'),
    url(r'^student_detail/', 'sdacademy.views.student_detail', name='student_detail'),
    #url(r'^quadratic/results/', 'sdacademy.views.quadratic_results',name='results'),




)

