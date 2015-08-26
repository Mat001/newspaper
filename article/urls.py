__author__ = 'matjaz'

from django.conf.urls import patterns, include, url

# add list of urls
urlpatterns = patterns('',
                       url(r'^all/$', 'article.views.articles'),
                       url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),)


