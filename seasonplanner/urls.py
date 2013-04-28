from django.conf.urls import patterns, url
from django.views.generic import DetailView
from seasonplanner.models import Season

from seasonplanner import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^seasons/$', views.seasons, name='seasons'),
    url(r'^seasons/(?P<pk>\d+)$',
        DetailView.as_view(model=Season, template_name='seasonplanner/detail.html'),
        name='detail'),
    url(r'^seasons/create/$', views.create, name='create'),
)
