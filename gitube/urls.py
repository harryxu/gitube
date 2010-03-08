from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # home page
    url(r'^$', 'apps.project.views.home', name='home'),

    # ssh key
    url(r'^account/public_keys/', include('apps.sshkey.urls')),
    # account
    url(r'^account/', include('apps.account.urls')),

    # register page
    url(r'^account/register/$', 'apps.account.views.register', name='user_register'),
    (r'^account/', include('django_authopenid.urls')),

    (r'^p/', include('apps.project.urls')),

    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
