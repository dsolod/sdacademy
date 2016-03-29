from django.conf.urls import patterns, url

from courses import views





urlpatterns = patterns('',
    url(r'^$', views.courses_list, name='courses_list'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson', views.add_lesson, name='add-lesson'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)

