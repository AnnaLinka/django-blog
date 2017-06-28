from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^aaa$', views.archive_post, name='archive_post'), #jesli nową stronę html to tu trzeba by wkleić name zmiennej (tak jak post_list), a później stworzyć w templates nowy plik costam.html
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

] # do tych wzorców będą sprawdzane adresy
