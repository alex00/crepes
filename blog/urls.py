from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('blog.views',
	url(r'^$', 'article.accueil'),
	url(r'^(?P<num>[0-9]+)/$', 'article.accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'article.lire'),
    url(r'^article/new$', 'article.new'),
    url(r'^contact/$', 'core.contact'),
    url(r'^login/$', 'user.login'),
    url(r'^logout/$', 'user.logout'),


)

