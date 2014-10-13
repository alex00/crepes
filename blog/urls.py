from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('blog.views',
	url(r'^$', 'accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'article'),
    url(r'^article/new$', 'article_new'),
    url(r'^contact/$', 'contact'),

)

