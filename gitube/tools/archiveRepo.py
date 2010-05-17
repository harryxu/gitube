import os

def archive(gitDir, saveDir, branch='master'):
    if gitDir.endswith('/'):
        gitDir += '.git'
    else:
        gitDir += '/.git'
    cmd = 'git --git-dir=' + gitDir + 'archive --format=zip ' + branch + ' > ' + saveDir
    #TODO replace os.system with which can obtain system output error message.
    os.system(cmd)
