from django.test import TestCase
from django.contrib.auth.models import User, Group

from gitube.project.models import *

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
        
        teams = Team.objects.order_by('id').all()
        self.flexAdmin     = teams[0]
        self.flexDeveloper = teams[1]
        self.flexGuest     = teams[2]

        self.flexRepo = Repository.objects.get(name='flex')

    def test_users_name_are_ok(self):
        self.assertEqual('harryxu', self.harryxu.username)
        self.assertEqual('sarah', self.sarah.username)
        self.assertEqual('chloe', self.chloe.username)
        self.assertEqual('jack', self.jack.username)
        self.assertEqual('kim', self.kim.username)
        self.assertEqual('clark', self.clark.username)

    def testCanRead_repo_user(self):
        """Test user can/not view repo."""
        # add chloe to flex repo as a developer
        RepositoryUserRoles.objects.create(
                user = self.chloe,
                group = self.developer,
                repo = self.flexRepo)
        
        self.assertTrue(self.flexRepo.canRead(self.harryxu))
        self.assertTrue(self.flexRepo.canRead(self.chloe))
        # Neither sarah is owner nor a user in flex repo.
        self.assertFalse(self.flexRepo.canRead(self.sarah))

    def testCanRead_repo_team_user(self):
        '''Test users in team can view repo'''
        self.flexAdmin.users.add(self.kim)
        self.flexDeveloper.users.add(self.clark)
        self.flexGuest.users.add(self.jack)
        
        self.assertTrue(self.flexRepo.canRead(self.kim))
        self.assertTrue(self.flexRepo.canRead(self.clark))
        self.assertTrue(self.flexRepo.canRead(self.jack))
        self.assertFalse(self.flexRepo.canRead(self.chloe))

    def testIsAdmin_repo_user(self):
        """Test user can/not edit repo."""
        self.assertTrue(self.flexRepo.isAdmin(self.harryxu))
        #self.assertTrue(self.flexRepo.isAdmin(self.chloe))
        self.assertFalse(self.flexRepo.isAdmin(self.sarah))
    
    def testIsAdmin_repo_team_user(self):
        pass

