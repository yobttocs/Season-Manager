from django.conf.urls import patterns, url

from seasonplanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^seasons/$', views.seasons, name='seasons'),

)
