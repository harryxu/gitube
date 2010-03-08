from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.sshkey.views',
    url(r'^$', 'index', name='public_keys_home'),
)

