from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def home(request):
    """docstring for start"""
    return render_to_response('home.html', 
            RequestContext(request))
