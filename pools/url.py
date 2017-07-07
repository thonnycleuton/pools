from django.conf.urls import url

from pools import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<pk>\d+)/$', views.question, name='question'),
]