from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

import django_authopenid
from django_authopenid.views import not_authenticated


@login_required
def index(request):
    """docstring for index"""
    return render_to_response('account/home.html', 
            RequestContext(request, {}))

@not_authenticated
def register(request):
    result = django_authopenid.views.register(request, send_email=False)

    if (request.POST and request.user is not None and not request.user.is_superuser):
        # We need active user by admin.
        request.user.is_active = False
        request.user.save()
    return result
