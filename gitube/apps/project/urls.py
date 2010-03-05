from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.project.views',
    # project level
    url(r'^create/$', 'createProject', name='create_project'),
    url(r'^(?P<pslug>[^/]+)/$', 'viewProject', name='view_project'),
    url(r'^(?P<pslug>\S+)/edit/$', 'editProject', name='edit_project'),

    # repo level
    url(r'^(?P<pslug>\S+)/newrepo/$', 'createRepository', name='create_repo'),
    url(r'^(?P<pslug>[^/]+)/(?P<rslug>[^/]+)/$', 'viewRepository', name='view_repo'),
    url(r'^(?P<pslug>[^/]+)/(?P<rslug>[^/]+)/edit/$', 'editRepository', name='edit_repo'),
);
