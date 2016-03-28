from django.conf.urls import url, patterns
from django.contrib import admin
from .views import (
    post_list,
    post_useful,
    post_events,
    post_other,
    post_create,
    post_about_us,
    post_detail,
    post_update,
    post_delete,
)


urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^useful/$', post_useful, name="useful"),
    url(r'^events/$', post_events, name="events"),
    url(r'^other/$', post_other, name="other"),
    url(r'^create/$', post_create, name="create"),
    url(r'^about/$', post_about_us, name="about"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),

]
