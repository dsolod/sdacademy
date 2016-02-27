from django.conf.urls import patterns, url

from courses import views





urlpatterns = patterns('',
    url(r'^$', views.courses_list, name='courses_list'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)

