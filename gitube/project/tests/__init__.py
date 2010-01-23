from django.test import TestCase
from django.contrib.auth.models import User

from gitube.project.models import *

class RepositoryTestCase(TestCase):
    fixtures = ['testing_data.yaml']

    def setUp(self):
        self.harryxu = User.objects.get(username='harryxu')
        self.sarah = User.objects.get(username='sarah')
        self.chloe = User.objects.get(username='chloe')
        self.flexRepo = Repository.objects.get(name='flex')

    def testCanRead_repo_user(self):
        self.assertTrue(self.flexRepo.canRead(self.harryxu))
        self.assertTrue(self.flexRepo.canRead(self.chloe))
        self.assertFalse(self.flexRepo.canRead(self.sarah))

    def testCanRead_repo_team_user(self):
        pass

    def testIsAdmin_repo_user(self):
        self.assertTrue(self.flexRepo.isAdmin(self.harryxu))
        self.assertTrue(self.flexRepo.isAdmin(self.chloe))
        self.assertFalse(self.flexRepo.isAdmin(self.sarah))
    
    def testIsAdmin_repo_team_user(self):
        pass

    def _addTeamUsers(self):
        
        pass
