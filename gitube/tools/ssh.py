#TODO lock file before write or remove key.

def makeAuthorizedKey(user, key):
    template = ('command="gitube-serve %(user)s",no-port-forwarding,'
              +'no-X11-forwarding,no-agent-forwarding,no-pty %(key)s')
    return template % {'user':user, 'key':key}

def writeKey(path, user, key):
    """docstring for writeKey"""
    fd = open(path, 'a')
    fd.write(makeAuthorizedKey(user, key)+'\n')
    fd.close()

def removeKey(path, user, key):
    pass
