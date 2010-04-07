from django import forms
from django.contrib.auth.models import Group

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

class MemberForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        groups = Group.objects.all()
        self.fields['group'].choices = [('', '-----')] + \
          [(group.id, group.name) for group in groups]

    username = forms.CharField(max_length=100)
    group = forms.ChoiceField()
