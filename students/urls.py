from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',

    #url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    #url(r'^add/', views.create, name='create'),
    url(r'^add/', views.StudentCreateView.as_view(), name='create'),
#    url(r'^edit/(?P<pk>\d+)/', views.edit, name='edit'),
	url(r'^edit/(?P<pk>\d+)/', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/', views.StudentDeleteView.as_view(), name='remove'),
    #url(r'^remove/(?P<pk>\d+)/', views.remove, name='remove'),
    #url(r'^(?P<course_id>=\d+)/$', views.list, name='list'),
    url(r'^(?P<course_id>=\d+)/$', views.StudentListView.as_view(), name='list'),
    url(r'^$', views.StudentListView.as_view(), name='list'),





)


