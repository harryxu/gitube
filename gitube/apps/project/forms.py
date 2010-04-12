from django import forms
from django.contrib.auth.models import User, Group

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
    username = forms.CharField(max_length=100)
    group_id = forms.ChoiceField()
    project_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        groups = Group.objects.all()
        self.fields['group_id'].choices = [('', '-----')] + \
          [(group.id, group.name) for group in groups]

    def save(self):
        purs = models.ProjectUserRoles(
                user=self.user, group=self.group, project=self.project)
        return purs.save()

    def clean(self):
        cleanedData = self.cleaned_data
        username = cleanedData.get('username')
        project_id = cleanedData.get('project_id')
        group_id = cleanedData.get('group_id')

        try:
            self.user = User.objects.get(username=username)
            self.project = models.Project.objects.get(id=project_id)
            self.group = Group.objects.get(id=group_id)
        except User.DoesNotExist:
            raise forms.ValidationError('User not exist, did you type put username?')
        except models.Project.DoesNotExist:
            raise forms.ValidationError('Project not exist.')
        except Group.DoesNotExist:
            raise forms.ValidationError('Group not exist.')

        try:
            models.ProjectUserRoles.objects.get(user=self.user, project=self.project)
            raise forms.ValidationError('User already in this project.')
        except models.ProjectUserRoles.DoesNotExist:
            pass

        return cleanedData
