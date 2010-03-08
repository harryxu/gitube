from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def index(request):
    """docstring for index"""
    pass

@login_required
def create(request):
    """docstring for create"""
    pass

@login_required
def edit(request, id):
    """docstring for edit"""
    pass
