from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    post_list,
    post_useful,
    post_events,
    post_other,
    post_create,
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
    url(r'^about/$', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),

]
