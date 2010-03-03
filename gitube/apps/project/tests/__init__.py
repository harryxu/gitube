from django.test import TestCase
from django.contrib.auth.models import User, Group

from gitube.apps.project.models import *

class RepositoryTestCase(TestCase):
    fixtures = ['testing_data.json']

    def setUp(self):
        users = User.objects.order_by('id').all()
        self.harryxu = users[0]
        self.sarah   = users[1]
        self.chloe   = users[2]
        self.jack    = users[3]
        self.kim     = users[4]
        self.clark   = users[5]
        
        groups = Group.objects.order_by('id').all()
        self.admin     = groups[0]
        self.developer = groups[1]
        self.guest     = groups[2]

        self.marsProj = Project.objects.get(owner=self.harryxu)

        repos = Repository.objects.order_by('id').filter(project=self.marsProj)
        self.flexRepo   = repos[0]
        self.cosmosRepo = repos[1]

    def testCanRead_repo_user(self):
        """Test user can/not view repo."""
        # add chloe to flex repo as a developer
        r = RepositoryUserRoles.objects.create(
                user = self.chloe,
                group = self.developer,
                repo = self.flexRepo)
        
        self.assertTrue(self.flexRepo.canRead(self.harryxu))
        self.assertTrue(self.flexRepo.canRead(self.chloe))
        # Neither sarah is owner nor a user in flex repo.
        self.assertFalse(self.flexRepo.canRead(self.sarah))

        r.delete()

    def testIsAdmin_repo_user(self):
        """Test user can/not edit repo."""
        r1 = RepositoryUserRoles.objects.create(
                user = self.chloe, group = self.admin, repo = self.flexRepo)
        r2 = RepositoryUserRoles.objects.create(
                user = self.sarah, group = self.developer, repo = self.flexRepo)

        self.assertTrue(self.flexRepo.isAdmin(self.harryxu))
        self.assertTrue(self.flexRepo.isAdmin(self.chloe))
        self.assertFalse(self.flexRepo.isAdmin(self.sarah))
        self.assertFalse(self.flexRepo.isAdmin(self.clark))

        r1.delete()
        r2.delete()

    def testCanRead_project_user(self):
        """docstring for testCanRead_project_user"""
        r1 = ProjectUserRoles.objects.create(
                user=self.kim, group=self.guest, project=self.marsProj)
        r2 = ProjectUserRoles.objects.create(
                user=self.jack, group=self.developer, project=self.marsProj)

        self.assertTrue(self.marsProj.canRead(self.kim))
        self.assertTrue(self.marsProj.canRead(self.jack))
        self.assertTrue(self.flexRepo.canRead(self.kim))
        self.assertTrue(self.flexRepo.canRead(self.jack))

        self.assertFalse(self.marsProj.canRead(self.chloe))
        self.assertFalse(self.flexRepo.canRead(self.chloe))

        r1.delete()
        r2.delete()

    def testIsAdmin_project_user(self):
        """docstring for testIsAdmin_project_user"""
        r1 = ProjectUserRoles.objects.create(
                user=self.kim, group=self.guest, project=self.marsProj)
        r2 = ProjectUserRoles.objects.create(
                user=self.jack, group=self.developer, project=self.marsProj)
        r3 = ProjectUserRoles.objects.create(
                user=self.chloe, group=self.admin, project=self.marsProj)

        self.assertTrue(self.marsProj.isAdmin(self.harryxu))
        self.assertTrue(self.marsProj.isAdmin(self.chloe))

        self.assertFalse(self.marsProj.isAdmin(self.kim))
        self.assertFalse(self.marsProj.isAdmin(self.jack))

        r1.delete()
        r2.delete()

