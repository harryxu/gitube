from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from gitube.apps.account import views as accountViews
from gitube.apps import project

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^account/register/$', accountViews.register, name='user_register'),
    (r'^account/', include('django_authopenid.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^p/', include(project.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
