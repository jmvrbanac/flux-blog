Title: Setting up pyenv
Date: 2016-5-31
Modified: 2016-5-31 10:00
Tags: Linux, Python, Virtual Envionment
Slug: setting-up-pyenv
Authors: John Vrbanac

One of the issues people who are developing Python always run into is being
able to install projects and their dependencies without the fear of messing up
your system Python. There are a number of ways to deal with this. The most
often recommended is to use virtual environments. While virtual environments
are awesome, they don't allow for you to test your code against various
versions of Python. This is where pyenv comes in.

pyenv is a fork of rbenv, a ruby project with the same purpose - Being a tool
to allow for you to easily switch between multiple interpreter versions. By
default, pyenv doesn't handle your virtual environments, but as I will show
you, it is very easy to integrate.

For these instructions, I'll be using Ubuntu 14.04; however, these instructions
should work for individuals using 16.04 as well.

## Installing system dependencies

As we'll be compiling various versions of Python, we'll need a number of system
dependencies prior to working with pyenv.

```shell
# Make sure we have updated package information
sudo apt-get update

# Install our dependencies
sudo apt-get install -y git build-essential python-dev libffi-dev libssl-dev \
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev
```

## Installing pyenv

```shell
# Download pyenv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv

# Add pyenv to your bash config
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload your bash config
source ~/.bashrc
```

## Adding Python versions

You should now be able to use the **pyenv** command; however, we still need
to add a couple of versions of Python to work with. To do this, we'll need
to use the **pyenv install** command.

```shell
# Install a version of Python 2.7 and 3.4
pyenv install 2.7.11
pyenv install 3.4.4

# Set those versions as our new defaults
pyenv global 2.7.11 3.4.4
```

Congratulations! You now have two fresh vanila versions of Python setup!

## Adding Virtual Environments to the mix

Now that we have our pristine versions of Python setup, we want to make sure
that they stay pristine between multiple projects. The way we deal with is with
virtual environments. There are many ways out there to work with virtual
environments; however, I'm going to focus on the one that I have found to be
the easiest to work with **pyenv-virtualenvwrapper**

```shell
# Download virtualenvwrapper plugin
git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper

# Add the plugin to your bash config
echo 'pyenv virtualenvwrapper' >> ~/.bashrc

# Reload your bash config
source ~/.bashrc
```

You'll notice that once you reload the config, it'll automatically install
a number of dependencies to required for virtualenvwrapper to work.

Now that we have everything installed, lets try a few commands:

```shell
# Creates a new virtual environment and activates it
mkvirtualenv my-env

# Deactivate the virtual environment
deactivate

# Activate a virtual environment
workon my-env

# Deactivate and remove a virtual environment
deactivate
rmvirtualenv my-env
```

That's it! You have successfully installed two pristine versions of Python and
have the ability to keep them pristine through the use of virtual environments.
