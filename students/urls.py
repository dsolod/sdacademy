from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
#	url(r'^(?P<course_id>=\d+)/$', views.IndexView.as_view(), name='index'),
#    url(r'^$', views.IndexView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<course_id>=\d+)/$', views.list, name='list'),
    url(r'^$', views.list, name='list'),
#    url(r'^(?P<pk>\d+)', views.DetailView.as_view(), name='detail'),




)


