from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gitube.apps.gitweb.views',
    url(r'^$', 'gitweb', name='gitweb'),
)


