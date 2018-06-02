from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NumberList.as_view(), name='index'),
    url(r'^create/$', views.NumberCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.NumberDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.NumberUpdate.as_view(), name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.NumberDeleteView.as_view(), name='delete'),
]