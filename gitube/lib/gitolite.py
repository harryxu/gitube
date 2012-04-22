"""
    gitolite conf file and ssh key managent.
    Inspired by gitolite:
    A Ruby interface for the gitolite git backend system.
    https://github.com/wingrunr21/gitolite
"""

class Conf(object):
    """gitolite conf file management """

    def __init__(self, filename='gitolite.conf'):
        self._filename = filename

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
        users = [v for k, v in self.permissions.items()]
        return 'repo %s\n    %s' % (self.name, '\n    '.join(users))
