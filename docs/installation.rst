Installation
============

Install gitolite
----------------

**Create user for git**::

    sudo adduser \
      --system \
      --shell /bin/sh \
      --gecos 'git version control' \
      --group \
      --disabled-password \
      --home /home/git \
      git

    # change user to git
    sudo su git

    # cd to git home
    cd

    # create bin dir
    mkdir bin

    # set PATH for user git
    echo "PATH=\$PATH:/home/git/bin\nexport PATH" > /home/git/.profile
    export PATH=/home/git/bin:$PATH

**Clone gitolite "g3" branch and install it**::

    # get the software
    git clone -b g3 git://github.com/sitaramc/gitolite

    # install it
    gitolite/install -ln

    # setup the initial repos with your key
    gitolite setup -pk your-name.pub

Now you can `Ctrl + d` to exit git user.
