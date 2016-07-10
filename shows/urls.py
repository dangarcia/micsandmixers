from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<show_id>[0-9]+)/$', views.show_detail, name='show_detail'),
    url(r'^stages/$', views.stage_index, name='stage_index'),
    url(r'^venues/$', views.venue_index, name='venue_index'),
]