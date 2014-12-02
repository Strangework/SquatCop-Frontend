from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^videotagger/', include('videotagger.urls', namespace='videotagger')),
    url(r'^admin/', include(admin.site.urls)),
)
