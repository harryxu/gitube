from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # home page
    url(r'^$', 'gitube.apps.project.views.home', name='home'),

    # gitweb
    url(r'^gitweb/', include('gitube.apps.gitweb.urls')),

    # ssh key
    url(r'^account/public_keys/', include('gitube.apps.sshkey.urls')),
    # account
    url(r'^account/', include('gitube.apps.account.urls')),

    # register page
    url(r'^account/register/$', 'gitube.apps.account.views.register', name='user_register'),
    (r'^account/', include('django_authopenid.urls')),

    (r'^p/', include('gitube.apps.project.urls')),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
