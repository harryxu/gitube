#TODO lock file before write or remove key.

import os

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
    key = makeAuthorizedKey(user, key) + '\n'
    tmp = '/tmp/%d.tmp' % os.getpid()
    infd = open(path, 'r')
    tmpfd = open(tmp, 'a')

    for line in infd:
        if line == key:
            continue
        tmpfd.write(line)

    infd.close()
    tmpfd.close()
    try:
        os.rename(tmp, path)
    except Exception, e:
        os.system('mv %s %s' % (tmp, path))
