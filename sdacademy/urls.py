from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from sdacademy import views
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^contact/$', views.contact),
    url(r'^student_list/$', views.student_list),
    url(r'^student_detail/$', views.student_detail),



)

