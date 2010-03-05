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
    if not project.canRead(request.user):
        raise Http404
        
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
            RequestContext(request, {'form':form,'action':'Create'}))

@login_required
def editProject(request, pslug):
    project = get_object_or_404(models.Project, slug=pslug)
    if not project.isAdmin(request.user):
        raise Http404
    if request.method == 'POST':
        form = forms.ProjectFrom(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(project)
    else:
        form = forms.ProjectFrom(instance=project)

    return render_to_response('project/project_form.html',
            RequestContext(request, {'form':form,'action':'Edit'}))


#########################  Repository #######################

@login_required
def viewRepository(request, pslug, rslug):
    """docstring for viewRepository"""
    pass

@login_required
def createRepository(request, pslug):
    """docstring for createRepo"""
    project = get_object_or_404(models.Project, slug=pslug)
    if not project.isAdmin(request.user):
        raise Http404
    if request.method == 'GET':
        form = forms.RepositoryForm()
    else:
        repo = models.Repository()
        repo.project = project
        form = forms.RepositoryForm(request.POST, instance=repo)
        if form.is_valid():
            form.save()
            return redirect(repo)

    return render_to_response('project/repository_form.html',
            RequestContext(request, {
                'form':form,
                'project':project,
                'action':'Create'}))

@login_required
def editRepository(request, pslug, rslug):
    #project = get_object_or_404(models.Project, slug=pslug)
    #repo = get_object_or_404(models.Repository, slug=rslug, project=project)
    #TODO
    pass
    
