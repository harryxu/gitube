from django.contrib import admin
from django.conf.urls.defaults import patterns
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from gitube.apps.sshkey import models

class SSHKeyAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(SSHKeyAdmin, self).get_urls()
        my_urls = patterns('', 
            ('^rebuild_authorized_keys/$', self.rebuildAuthorizedKeys),
        )
        return my_urls + urls

    def rebuildAuthorizedKeys(self, request):
        self.message_user(request, _('authorized_keys rebuild successed!'))
        models.rebuildAuthorizedKeys()
        return HttpResponseRedirect('/admin/sshkey/sshkey/')

admin.site.register(models.SSHKey, SSHKeyAdmin)
