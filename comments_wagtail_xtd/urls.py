from __future__ import absolute_import, unicode_literals
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.pages, name='comments_wagtail_xtd_pages'),
    re_path(r'^(?P<pk>\d+)/$', views.comments, name='comments_wagtail_xtd_comments'),
    re_path(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/thread/$',
        views.comment_thread, name='comments_wagtail_xtd_comment_thread'),
    re_path(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/update/(?P<action>publish|unpublish|hide|show)/$',
        views.update, name='comments_wagtail_xtd_publication'),
]
