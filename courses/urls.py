from django.conf.urls import patterns, url

from courses import views





urlpatterns = patterns('',
    url(r'^$', views.courses_list, name='courses_list'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/', views.add, name='add'),
    url(r'^edit/(?P<pk>\d+)/', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/', views.remove, name='remove'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson/', views.add_lesson, name='add-lesson'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)

