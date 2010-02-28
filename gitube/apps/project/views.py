from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from gitube.apps.project import models

def home(request):
    """docstring for start"""
    viewData = {}
    if request.user.is_authenticated:
        #viewData['projects'] = models.Project.objects.get(owner=request.user)
        pass
    return render_to_response('home.html', 
        RequestContext(request, viewData))
