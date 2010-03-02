from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from gitube.apps.project import models, forms

def home(request):
    """docstring for start"""
    viewData = {}
    if request.user.is_authenticated:
        viewData['projects'] = models.Project.objects.filter(owner=request.user)
    return render_to_response('home.html', 
            RequestContext(request, viewData))


#########################  Project #######################

def viewProject(request, pslug):
    """docstring for viewProject"""
    project = get_object_or_404(models.Project, slug=pslug)
    return render_to_response('project/view_project.html',
            RequestContext(request, {'project':project}))

@login_required
def createProject(request):
    """Create a new project"""
    if request.method == 'GET':
        form = forms.ProjectFrom()
    else:
        project = models.Project()
        project.owner = request.user
        form = forms.ProjectFrom(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(project)

    return render_to_response('project/project_form.html',
            RequestContext(request, {'form':form}))


#########################  Repository #######################

def createRepository(request):
    """docstring for createRepo"""
    pass

