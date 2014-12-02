from django.conf.urls import patterns, url

from videotagger import views

urlpatterns = patterns('',
  url(r'^$', views.index, name="index"),
  url(r'^upload/$', views.upload, name="upload"),
  #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
)
