from django.test import TestCase
from django.contrib.auth.models import User

from gitube.project.tests import *
from gitube.project.models import *

class RepositoryTestCase(TestCase):
    fixtures = ['testing_data.yaml']

    def setUp(self):
        self.harryxu = User.objects.get(username='harryxu')
        self.sarah = User.objects.get(username='sarah')
        self.flexRepo = Repository.objects.get(name='flex')

    def testCanRead_repo_user(self):
        self.assertTrue(self.flexRepo.canRead(self.harryxu))
        self.assertFalse(self.flexRepo.canRead(self.sarah))

    def testCanRead_repo_team_user(self):
        pass
    
