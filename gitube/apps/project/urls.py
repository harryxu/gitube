from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('gitube.apps.project.views',
    # project level
    url(r'^create/$', 'createProject', name='create_project'),
    url(r'^(?P<pslug>[^/]+)/$', 'viewProject', name='view_project'),
    url(r'^(?P<pslug>[^/]+)/edit/$', 'editProject', name='edit_project'),

    # project members
    url(r'^(?P<pslug>[^/]+)/members/$', 'listProjectMembers', name='list_project_members'),
    url(r'^(?P<pslug>[^/]+)/members/add/$', 'addProjectMember', name='add_project_member'),
    url(r'^(?P<pslug>[^/]+)/members/del/(?P<userId>\d+)/$', 
            'removeProjectMember', name='del_project_member'),

    # repo level
    url(r'^(?P<pslug>\S+)/newrepo/$', 'createRepository', name='create_repo'),
    url(r'^(?P<pslug>[^/]+)/r/(?P<rslug>[^/]+)/$', 'viewRepository', name='view_repo'),
    url(r'^(?P<pslug>[^/]+)/r/(?P<rslug>[^/]+)/edit/$', 'editRepository', name='edit_repo'),

);
