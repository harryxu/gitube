"""
    gitolite conf file and ssh key managent.
    Inspired by gitolite:
    A Ruby interface for the gitolite git backend system.
    https://github.com/wingrunr21/gitolite
"""

class Conf(object):
    """gitolite conf file management """

    def __init__(self, filename='gitolite.conf'):
        self.filename = filename
        self.groups = {}
        self.repos = {}

    def add_group(self, group):
        self.groups[group.name] = group

    def del_group(self, group_name):
        del self.groups[group_name]

    def has_group(self, group_name):
        return group_name in self.groups

    def get_group(self, group_name):
        if not self.has_groupd(group_name):
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

    def __str__(self):
        groups = [str(group) for group in self.groups.values()]
        repos = [str(repo) for repo in self.repos.values()]

        return '%s\n\n%s' % ('\n'.join(groups), '\n\n'.join(repos))


class Group(object):
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        if not user in self.users:
            self.users.append(user)

    def del_user(self, user):
        self.users.remove(user)

    def __str__(self):
        return '%s = %s' % (self.name, ' '.join(self.users))
        

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
