from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.quadratic_results, name='quadratic_results'),
)

