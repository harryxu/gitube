from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.account.views',
    url(r'^/$', 'index', name='account_home'),
)

