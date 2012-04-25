from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
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
    user = request.user

    # 'email' in request.POST.keys() indicate is creating a new account.
    if (request.POST and 'email' in request.POST.keys()
            and user is not None 
            and not user.is_superuser
            and not user.is_anonymous()):
        # We need active user by admin.
        user.is_active = False
        user.save()
    return result
