from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.project.views',
    # project level
    url(r'^create/$', 'createProject', name='create_project'),
    url(r'^(?P<pslug>\S+)/edit/$', 'editProject', name='edit_project'),
    url(r'^(?P<pslug>\S+)/$', 'viewProject', name='view_project'),

    # repo level
    url(r'^(?P<pslug>\S+)/newrepo/$', 'createRepository', name='create_repo'),
);
