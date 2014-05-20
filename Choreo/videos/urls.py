from django.conf.urls import patterns, url
from videos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<video_id>\d+)/$', views.detail, name='detail')
)
