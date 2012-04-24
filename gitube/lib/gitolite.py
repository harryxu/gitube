"""
    gitolite conf file and ssh key managent.
    Inspired by gitolite:
    A Ruby interface for the gitolite git backend system.
    https://github.com/wingrunr21/gitolite
"""

import re

class Conf(object):
    """gitolite conf file management """

    def __init__(self, filename='gitolite.conf'):
        self.filename = filename

        self.groups = {}
        self.group_names = [] # keep group definition order

        self.repos = {}

    def add_group(self, group):
        self.groups[group.name] = group
        self.group_names.append(group.name)

    def del_group(self, group_name):
        if self.has_group(group_name):
            del self.groups[group_name]
            self.group_names.remove(group_name)

    def has_group(self, group_name):
        return group_name in self.groups

    def get_group(self, group_name):
        if not self.has_group(group_name):
            return None
        return self.groups[group_name]

    def add_repo(self, repo):
        self.repos[repo.name] = repo

    def del_repo(self, repo_name):
        del self.repos[repo_name]

    def has_repo(self, repo_name):
        return repo_name in self.repos

    def get_repo(self, repo_name):
        if not self.has_repo(repo_name):
            return None
        return self.repos[repo_name]

    def parse_conf(self, conf_str):
        lines = conf_str.splitlines(True)
        for line in lines:
            line = line.strip()

            # match repo definition
            if self._rematch('^repo\s+(.+)', line):
                repo_names = self._matches.group(1).strip().split(' ')
                for reponame in repo_names:
                    reponame = reponame.strip()
                    if reponame:
                        self.add_repo(Repo(reponame))

            # match permission definition in repo
            elif self._rematch('^(-|R|W|RW\+?)\s+(\S+)?\s*=\s+(.+)', line):
                perm = self._matches.group(1)
                refex = self._matches.group(2)
                if not refex:
                    refex = ''
                users = self._matches.group(3).split(' ')
                for reponame in repo_names:
                    self.get_repo(reponame).add_permission(perm, refex, *users)

            # match group definition
            elif self._rematch('^@(\S+)\s+=\s+(.+)', line):
                group_name = self._matches.group(1)
                users = self._matches.group(2).split(' ')

                if not self.has_group(group_name):
                    self.add_group(Group(group_name))

                self.get_group(group_name).add_users(*users)

    def _rematch(self, pattern, string, flags=0):
        matches = re.match(pattern, string, flags)
        self._matches = matches
        return matches

    def __str__(self):
        groups = [str(self.groups[name]) for name in self.group_names]
        repos = [str(repo) for repo in self.repos.values()]

        return '%s\n\n%s' % ('\n'.join(groups), '\n\n'.join(repos))


class Group(object):
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_users(self, *users):
        for user in users:
            if not user in self.users:
                self.users.append(user)

    def del_users(self, *users):
        for user in users:
            if user in self.users:
                self.users.remove(user)

    def has_user(self, user):
        return user in self.users

    def __str__(self):
        return '@%s = %s' % (self.name, ' '.join(self.users))
        

class Repo(object):
    """gitolite repo"""

    def __init__(self, name):
        self.name = name
        self.permissions = {}

    def add_permission(self, perm, refex='', *users):
        for user in users:
            key = user
            if perm == '-':
                key = user + '-'

            self.permissions[key] = '%s %s = %s' % (perm, refex, user)

    def del_permission(self, *users):
        for user in users:
            if user in self.permissions:
                del self.permissions[user]
            if user + '-' in self.permissions:
                del self.permissions[user + '-']

    def __str__(self):
        users = [perm for perm in self.permissions.values()]
        return 'repo %s\n    %s' % (self.name, '\n    '.join(users))
