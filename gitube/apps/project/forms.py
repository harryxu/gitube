from gitube.forms import BaseModelForm
from gitube.apps.project import models


class ProjectFrom(BaseModelForm):
    class Meta:
        model = models.Project
        fields =('name', 'slug', 'description', 'is_public')
