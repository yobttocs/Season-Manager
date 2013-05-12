from django.conf.urls import patterns, url
from django.views.generic import DetailView
from seasonplanner.models import Season, Week

from seasonplanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^seasons/$', views.seasons, name='seasons'),
    url(r'^seasons/(?P<pk>\d+)$',
        views.SeasonDetail.as_view(model=Season, template_name='seasonplanner/detail.html'),
        name='detail'),
    url(r'^seasons/create/$', views.create, name='create'),
    url(r'^weeks/(?P<pk>\d+)$',
        DetailView.as_view(model=Week, template_name='seasonplanner/week_detail.html'),
        name='week_detail'),
)
