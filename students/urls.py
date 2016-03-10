from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^add/', views.create, name='create'),
    url(r'^edit/(?P<pk>\d+)', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)', views.remove, name='remove'),
    url(r'^(?P<course_id>=\d+)/$', views.list, name='list'),
    url(r'^$', views.list, name='list'),





)


