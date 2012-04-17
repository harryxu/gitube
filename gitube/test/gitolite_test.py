#!/usr/bin/env python
# encoding: utf-8

import unittest
from gitube.lib import gitolite

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



if __name__ == '__main__':
    unittest.main()
