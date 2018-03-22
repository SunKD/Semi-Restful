from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^users/(?P<id>\d+)$', views.update),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^create$', views.create)

]