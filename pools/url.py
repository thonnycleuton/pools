from django.conf.urls import url

from pools import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<pk>\d+)/$', views.question, name='question'),
    url(r'^question/(?P<pk>\d+)/results/$', views.result, name='result'),
    url(r'^question/(?P<pk>\d+)/vote/$', views.vote, name='vote'),
    url(r'^question/(?P<pk>\d+)/manage/$', views.manage, name='manage'),
    url(r'^question/(?P<pk>\d+)/remove/$', views.remove, name='remove'),
    url(r'^question/(?P<pk>\d+)/status/$', views.status, name='status'),
]