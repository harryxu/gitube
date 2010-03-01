from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.project.views',
    url(r'^create/$', 'createProject', name='create_project'),
    url(r'^(?P<pslug>\S+)/$', 'viewProject', name='view_project'),
    url(r'^(?P<pslug>\S+)/newrepo/$', 'createRepository', name='create_repo'),
);
