#!/usr/bin/env python
# encoding: utf-8

import unittest
from gitube.lib import gitolite

class ConfTest(unittest.TestCase):

    def test_misc(self):
        group_admin = gitolite.Group('admin')
        group_admin.add_user('boss')

        group_dev = gitolite.Group('developer')
        group_dev.add_user('harry')
        group_dev.add_user('harryxu')

        repo_gitube = gitolite.Repo('gitube')
        repo_gitube.add_permission('RW', '', 'harry', 'harryxu')
        repo_gitube.add_permission('-', 'master', 'harry')

        repo_test = gitolite.Repo('test')
        repo_test.add_permission('RW', '', 'harry', 'harryxu')

        conf = gitolite.Conf();
        conf.add_group(group_admin)
        conf.add_group(group_dev)
        conf.add_repo(repo_gitube)
        conf.add_repo(repo_test)

        self.assertTrue(conf.has_group('developer'))
        self.assertTrue(conf.has_group('admin'))
        conf.del_group('developer')
        self.assertFalse(conf.has_group('developer'))

        self.assertTrue(conf.has_repo('gitube'))
        self.assertTrue(conf.has_repo('test'))
        conf.del_repo('test')
        self.assertFalse(conf.has_group('test'))

class GroupTest(unittest.TestCase):

    def test_add_user(self):
        group = gitolite.Group('developer')
        group.add_user('harry')
        group.add_user('harryxu')

        self.assertEqual(str(group), '@developer = harry harryxu')

    def test_del_user(self):
        group = gitolite.Group('developer')
        group.add_user('harry')
        group.add_user('flash')

        self.assertEqual(str(group), '@developer = harry flash')

        group.del_user('harry')

        self.assertEqual(str(group), '@developer = flash')

class RepoTest(unittest.TestCase):

    def test_add_permision(self):
        repo = gitolite.Repo('gitube')
        repo.add_permission('RW', '', 'harry', 'harryxu')
        repo.add_permission('-', 'master', 'harry')
        repo_str = str(repo)

        self.assertRegexpMatches(repo_str, 'repo\sgitube');
        self.assertRegexpMatches(repo_str, 'RW\s+=\sharry');
        self.assertRegexpMatches(repo_str, 'RW\s+=\sharryxu');
        self.assertRegexpMatches(repo_str, '-\smaster\s+=\sharry');

    def test_del_permission(self):
        repo = gitolite.Repo('gitube')
        repo.add_permission('RW', '', 'harry')
        repo.add_permission('-', 'master', 'harry')
        repo_str = str(repo)

        self.assertRegexpMatches(repo_str, 'RW\s+=\sharry');
        self.assertRegexpMatches(repo_str, '-\smaster\s+=\sharry');

        repo.del_permission('harry')
        repo_str = str(repo)

        self.assertNotRegexpMatches(repo_str, 'RW\s+=\sharry')
        self.assertNotRegexpMatches(repo_str, '-\smaster\s+=\sharry');




if __name__ == '__main__':
    unittest.main()
