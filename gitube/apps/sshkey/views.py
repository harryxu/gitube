from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from gitube.apps.sshkey import models, forms

@login_required
def index(request):
    """docstring for index"""
    keys = models.SSHKey.objects.filter(user=request.user)
    return render_to_response('sshkey/home.html',
            RequestContext(request, {'keys':keys}))

@login_required
def create(request):
    """docstring for create"""
    if request.method == 'POST':
        key = models.SSHKey()
        key.user = request.user
        form = forms.KeyForm(request.POST, instance=key)
        if form.is_valid():
            form.save()
            return redirect('public_keys_home')
    else:
        form = forms.KeyForm()
    return render_to_response('sshkey/form.html',
            RequestContext(request, {
                'form': form, 
                'action': 'Create'}))

@login_required
def edit(request, id):
    """docstring for edit"""
    key = get_object_or_404(models.SSHKey, pk=id, user=request.user)
    if request.method == 'POST':
        form = forms.KeyForm(request.POST, instance=key)
        if form.is_valid():
            form.save()
            return redirect('public_keys_home')
    else:
        form = forms.KeyForm(instance=key)
    return render_to_response('sshkey/form.html',
            RequestContext(request, {
                'form': form, 
                'action': 'Edit'}))

@login_required
def delete(request, id):
    """docstring for delete"""
    key = get_object_or_404(models.SSHKey, pk=id, user=request.user)
    key.delete()
    return redirect('public_keys_home')
