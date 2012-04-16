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
        self._name = name
        

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

            self.permissions[key] = {
                'perm': perm,
                'refex': refex,
                'user': user,
            }

    def del_permission(self, users):
        pass

    def __repr__(self):
        pass

