from django.conf.urls.defaults import patterns, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^account/', include('django_authopenid.urls')),
    (r'^admin/', include(admin.site.urls)),
)
