from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^videos/', include('videos.urls', namespace = "videos")),
    url(r'^admin/', include(admin.site.urls)),
)