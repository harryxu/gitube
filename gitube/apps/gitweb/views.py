import os, sys, subprocess, httplib
from cStringIO import StringIO

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings

@login_required
def gitweb(request):
    cigenv = {
            'REQUEST_METHOD': request.method,
            'QUERY_STRING': request.META['QUERY_STRING'],
            'GITWEB_SITENAME': 'gitub',
            'GITWEB_CONFIG': getattr(settings, 'PROJECT_PATH') + '/gitweb.conf',
    }
    os.environ.update(cigenv)

    p = subprocess.Popen([getattr(settings, 'PROJECT_PATH') + '/gitweb.cgi'],
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
    )

    stdout, stderr = p.communicate()

    res = httplib.HTTPResponse(FakeSock(), method='GET')
    res.fp = StringIO(stdout)
    res.begin()

    headers = res.getheaders()
    if not headers:
        msg = httplib.HTTPMessage(StringIO(stdout))
        headers = msg.headers
    else:
        meg = res.msg

    #remove headers
    while True:
        line = res.fp.readline()
        if line == '\r\n': break

    response = HttpResponse(res.read(), mimetype=msg.getheader('content-type'))
    for item in headers:
        response[item[0]] = item[1]
    return response

class FakeSock(object):
    def makefile(self, mode, bufsize):
        pass

