from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newspaper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'newspaper.views.home'),
    url(r'^article1/$', 'article.views.article_1'),
    url(r'^article2/$', 'article.views.article_2'),
    url(r'^article3/$', 'article.views.article_3'),
    url(r'^article_t/$', 'article.views.article_aaa_template'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^articles/', include('article.urls')),
)
# above - no need for url as prefix when you use includej