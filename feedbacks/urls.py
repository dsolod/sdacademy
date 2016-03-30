from django.conf.urls import patterns, url

from feedbacks import views





urlpatterns = patterns('',
    url(r'^$', views.FeedbackView.as_view(), name='index'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

)

