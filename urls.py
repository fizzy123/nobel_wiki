from django.conf.urls import patterns, url

from wiki import views 

urlpatterns = patterns('wiki.views',
	url(r'^$', 'display', name='index'),
	url(r'^(?P<name>[^ \t\n\r\f\v/]+)/$', 'display', name='display'),
	url(r'^edit/(?P<name>[^ \t\n\r\f\v/]+)/$', 'edit', name='edit'),
)
