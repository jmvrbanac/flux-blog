Title: Testing multiple Python versions in Codeship
Date: 2015-1-31
Modified: 2015-1-31 12:00
Tags: Development, Engineering, Python, Environment, CI
Slug: testing_multiple_python_versions_in_codeship
Authors: John Vrbanac

Lately, I've been looking for better CI-CD tools for my projects. I heard 
about [Codeship](https://codeship.com) on a Podcast and I thought I would 
give it a shot. Infact, I'm now using Codeship to build and deploy the 
contents of this blog. Unfortunately, they currently don't have the greatest
setup for Python. Considering I still wanted to try them out, I put together
a script to add proper Python support using PyEnv. Here is how you can do it
as well.

1. Go to your project's settings
2. Click on "Test"
3. Under "modify your setup commands" use the following script

```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 2.7.9
pyenv install 3.3.6
pyenv install 3.4.2
pyenv install pypy-2.4.0

pyenv global 2.7.9 3.4.2 3.3.6 pypy-2.4.0
```

Congratulations! You now have fresh versions of 2.7.9, 3.3.6, 3.4.2, 
and PyPy 2.4.0 available so that you can test your Python code against in
your Codeship project. Perhaps, in the future, Codeship will improve their
Python project support so that this workaround isn't needed.
