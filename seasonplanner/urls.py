from django.conf.urls import patterns, url

from seasonplanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^seasons/$', views.seasons, name='seasons'),
    url(r'^seasons/(?P<season_id>\d+)$', views.detail, name='detail'),
    url(r'^seasons/create/$', views.create, name='create'),
)
