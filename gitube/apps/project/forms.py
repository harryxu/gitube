from django import forms

from gitube.forms import BaseModelForm
from gitube.apps.project import models


class ProjectFrom(BaseModelForm):
    class Meta:
        model = models.Project
        fields = ('name', 'slug', 'description', 'is_public')

class RepositoryForm(BaseModelForm):
    class Meta:
        model = models.Repository
        fields = ('name', 'slug', 'description')

class ProjectMemberForm(BaseModelForm):
    class Meta:
        model = models.ProjectUserRoles
        widgets = {
                'project': forms.HiddenInput(),
        }
