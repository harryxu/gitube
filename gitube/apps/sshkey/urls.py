from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.sshkey.views',
    url(r'^$', 'index', name='public_keys_home'),
    url(r'^create/$', 'create', name='create_public_key'),
    url(r'^(?P<id>\d+)/edit/$', 'edit', name='edit_public_key'),
    url(r'^(?P<id>\d+)/del/$', 'delete', name='del_public_key'),
)

