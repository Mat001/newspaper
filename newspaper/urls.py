from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newspaper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'newspaper.views.home'),
    url(r'^title/$', 'article.views.title_aaa'),
    url(r'^title_t/$', 'article.views.title_aaa_template'),

    url(r'^admin/', include(admin.site.urls)),


    # url(r'^title_template/$', 'article.views.title_aaa_template'),



)
